from dash import dcc
from dash import html
from dash.dependencies import Input, Output

import dash_holoniq_components as dhc

from app import app
from .apps import app1, app2


app.layout = html.Div([
    dhc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])

# This is an exmple of a multi-page app.
#
# see "Structuring a Multi-Page App"https://dash.plotly.com/urls

@app.callback(Output('page-content', 'children'),
              Input('url', 'pathname'))
def display_page(pathname):
    if pathname == '/apps/app1':
        return app1.layout
    elif pathname == '/apps/app2':
        return app2.layout
    else:
        return '404'


# python -m examples.multi_page.index

if __name__ == '__main__':
    print("Visit http://default:8050/apps/app1")
    app.run_server(host='0.0.0.0', debug=False)
