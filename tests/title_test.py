import dash
from dash import html, dcc
from dash.dependencies import Input, Output

import dash_holoniq_components as dhc

def site_layout(app):

     # Process browser location change

    @app.callback([Output('title', 'title'), Output('page-ref', 'children')], [Input('loc', 'pathname')])
    def _location_callback(pathname):
        title = 'My Site: {}'.format(pathname)
        return title, title

    return html.Div([
        dhc.PageTitle(title='My Site', id='title'),
        dhc.Location(id='loc'),
        html.H2(id='page-ref'),
        dcc.Link('page1', id='page1', href='/page1', refresh=False),
        dcc.Link('page2', id='page2', href='/page2', refresh=False)
    ])


def test_title(dash_duo):
    app = dash.Dash(__name__, suppress_callback_exceptions=True)
    app.layout = site_layout(app)

    dash_duo.start_server(app)

    SITE = dash_duo.server_url

    assert dash_duo.wait_for_text_to_equal("#page-ref", "My Site: /", timeout=20)
    assert dash_duo.driver.title == "My Site: /"

    # Select Page 1 using link

    page1_link = dash_duo.find_element("#page1")
    page1_link.click()

    assert dash_duo.wait_for_text_to_equal("#page-ref", "My Site: /page1", timeout=20)
    assert dash_duo.driver.title == "My Site: /page1"

    # Select page 2 using link

    page2_link = dash_duo.find_element("#page2")
    page2_link.click()

    assert dash_duo.wait_for_text_to_equal("#page-ref", "My Site: /page2", timeout=20)
    assert dash_duo.driver.title == "My Site: /page2"

    # Select page 1 using location

    dash_duo.server_url = SITE + "/page1"
    assert dash_duo.wait_for_text_to_equal("#page-ref", "My Site: /page1", timeout=20)
    assert dash_duo.driver.title == "My Site: /page1"

    # Return to previous page using browser history

    dash_duo.driver.back()
    assert dash_duo.wait_for_text_to_equal("#page-ref", "My Site: /page2", timeout=20)
    assert dash_duo.driver.title == "My Site: /page2"

    # Return to next page using browser history

    dash_duo.driver.forward()
    assert dash_duo.wait_for_text_to_equal("#page-ref", "My Site: /page1", timeout=20)
    assert dash_duo.driver.title == "My Site: /page1"
