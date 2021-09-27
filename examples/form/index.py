from utils import log

from dash import html
from dash.dependencies import Input, Output

import dash_holoniq_components as dhc

from examples.form import default_page, user_page, signin_form, checkbox_form, user_profile

from app import app, serve_app

# Return static layout common to all pages

def page_layout():

    # Define page content

    page_layouts = {
        'default': default_page(),
        'user' : user_page(),
        'signin' : signin_form(),
        'checkbox' : checkbox_form(),
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

def create_app():
    app.layout = page_layout()
    return app

# python -m examples.form.index

if __name__ == '__main__':
    app = create_app()
    serve_app(app, '/checkbox')
