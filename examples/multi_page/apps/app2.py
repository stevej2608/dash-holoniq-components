import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output

from app import app

NOUPDATE = dash.no_update

layout = html.Div([
    dcc.Location(id='app-2-loc', refresh=False),
    html.H3('App 2'),
    dcc.Dropdown(
        id='app-2-dropdown',
        options=[
            {'label': 'App 2 - {}'.format(i), 'value': i} for i in [
                'NYC', 'MTL', 'LA'
            ]
        ]
    ),
    html.Div(id='app-2-display-value'),
    dcc.Link('Go to App 1 NYC', href='/apps/app1?state=NYC')
])

# Use dropdown value event to update the text on the page

@app.callback(
    Output('app-2-display-value', 'children'),
    Input('app-2-dropdown', 'value'))
def display_value(value):
    return 'You have selected "{}"'.format(value)

# Use dropdown value event to update the browser addrress bar

@app.callback( Output('app-2-loc', 'search'), Input('app-2-dropdown', 'value'))
def update_url(value):
    return '?state=' + value if value else NOUPDATE

# Use browser address bar search event to update the dropdown 
# value.
# 
# eg: http://localhost/apps/app2?state=LA

@app.callback( Output('app-2-dropdown', 'value'), Input('url', 'search'))
def update_dropdown(value):
    value = value.replace('?state=', '') if value else None
    return value
