from utils import logging, log

from dash import html
from dash.dependencies import Input, Output

import dash_holoniq_components as dhc

from examples.form import default_page, user_page, signin_form, user_profile

from app import app

# Return static layout common to all pages

def page_layout():

    # Define page content

    page_layouts = {
        'default': default_page(),
        'user' : user_page(),
        'signin' : signin_form(),

    }


    # Process browser location change. Select the page content based on the location

    @app.callback([Output('router', 'switch'), Output('title', 'title')], [Input('loc', 'pathname')])
    def _router_callback(pathname):
        route = 'default'
        title = 'My Site: {}'.format(user_profile.user)

        log.info('pathname=%s', pathname)

        if pathname:
            pathname = pathname[1:]

            if pathname in page_layouts:
                route = pathname

        return route, title

    # Return static content common to all pages on the site

    (routes, children) = zip(*page_layouts.items())

    return html.Div([
        dhc.PageTitle(title='My Site', id='title'),
        dhc.Location(id='loc'),
        dhc.LayoutRouter(children, routes=routes, id='router')

    ])

def form_example():
    # Turn off werkzeug logging as it's very noisy

    aps_log = logging.getLogger('werkzeug')
    aps_log.setLevel(logging.ERROR)

    print('\nvisit http://default:8050/\n')

    app.layout = page_layout()
    app.run_server(host='0.0.0.0', debug=False, threaded=False, dev_tools_serve_dev_bundles=True)

# python -m examples.form.index

if __name__ == '__main__':
    form_example()
