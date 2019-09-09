from utils import logging, log

import dash
from dash.dependencies import Input, Output

import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_core_components as dcc

from examples.signin_form import layout as signin_form

from examples.user_profile import user_profile
from examples.user_profile import layout as user_profile_layout

import dash_holoniq_components as dhc
from app import app


def page_layout():

    page_layouts = {
        'signin' : signin_form(),
        'default' : user_profile_layout()
    }

    (routes, children) = zip(*page_layouts.items())

    @app.callback([Output('router', 'switch'), Output('title', 'title')], [Input('loc', 'pathname')])
    def _router_callback(pathname):
        route = 'default'
        title = 'My Site: {}'.format(user_profile.user)
        
        log.info('_router_callback pathname=%s', pathname)

        if pathname:
            pathname = pathname[1:]
            if pathname in page_layouts:
                route = pathname

            if route == 'signin' and user_profile.user_signed_in():
                route = 'default'


        return route, title


    return html.Div([
        dhc.PageTitle(title='My Site', id='title'),
        dcc.Location(id='loc'),
        dhc.LayoutRouter(children, routes=routes, id='router')

    ])


def dash_layout_refresh():
    """Clear the Dash layout & callback state prior rebuilding, 
    it's as if this is the first call prior to calling dash.run_server()
    
    Returns:
        [obj] -- Dash layout tree
    """
    try:

        app.callback_map = {}
        app._layout = None

        # Rebuild everything

        layout = page_layout()

    finally:

        # Allow dash to call us again on the next refresh

        app._layout = dash_layout_refresh

    return layout


if __name__ == '__main__':

    # Turn off werkzeug logging as it's very noisy

    aps_log = logging.getLogger('werkzeug')
    aps_log.setLevel(logging.ERROR)

    print('\nvisit http://localhost:8050/\n')

    app.layout = dash_layout_refresh
    app.run_server(debug=False, threaded=False)
