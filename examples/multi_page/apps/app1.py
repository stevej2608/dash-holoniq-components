import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output

from app import app

NOUPDATE = dash.no_update

layout = html.Div([
    html.H3('App 1'),
    dcc.Location(id='app-1-loc', refresh=False),
    dcc.Dropdown(
        id='app-1-dropdown',
        options=[
            {'label': 'App 1 - {}'.format(i), 'value': i} for i in [
                'NYC', 'MTL', 'LA'
            ]
        ]
    ),
    html.Div(id='app-1-display-value'),
    dcc.Link('Go to App 2 MTL', href='/apps/app2?state=MTL')
])

# Use dropdown value event to update the text on the page

@app.callback(
    Output('app-1-display-value', 'children'),
    Input('app-1-dropdown', 'value'))
def display_value(value):
    return 'You have selected "{}"'.format(value)

# Use dropdown value event to update the browser addrress bar

@app.callback( Output('app-1-loc', 'search'), Input('app-1-dropdown', 'value'))
def update_url(value):
    return '?state=' + value if value else NOUPDATE

# Use browser address bar search event to update the dropdown 
# value.
# 
# eg: http://localhost/apps/app1?state=MTL

@app.callback( Output('app-1-dropdown', 'value'), Input('url', 'search'))
def update_dropdown(value):
    value = value.replace('?state=', '') if value else None
    return value
