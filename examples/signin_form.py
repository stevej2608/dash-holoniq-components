from utils import logging, log

import dash
from dash.dependencies import Input, Output

import dash_bootstrap_components as dbc
import dash_holoniq_components as dhc
import dash_html_components as html

from app import app

from .user_profile import user_profile

NOUPDATE = dash.no_update

"""
Shows the Alert, InputWithIcon, PasswordWithShow and Form components
"""

def formFields():
    return [
        dhc.Alert(id='flash', className="alert alert-danger", role="alert"),
        dbc.FormGroup([
            dbc.Label('Name'),
            dhc.InputWithIcon(type='name', id ='name', name='name', 
                              autoComplete='name', placeholder='Enter name', 
                              icon='fa fa-user', tooltip='Hello Big Joe')
        ]),
        dbc.FormGroup([
            dbc.Label('Password'),
            dhc.PasswordWithShow(name='password', id='password', autoComplete='password', 
                                 placeholder='Enter password', 
                                 tooltip='Hide/Show password')
        ]),

        html.Div(
            html.Button('Sign In', type="submit", disabled=False, className="btn btn-primary btn-block"),
            className="form-group m-0")
    ]

def layout():

    @app.callback([Output('signin-redirect', 'href'), Output('flash', 'children')], [Input('form','form_data')])
    def _callback(form_data):
        redirect = NOUPDATE
        flash = None

        if form_data:
            if form_data['name'] == '':
                flash = 'Enter your name'
            elif len(form_data['password']) < 8:
                flash = 'Password must be at least 8 characters'
            else:
                log.info('form data: %s', form_data)
                user_profile.set_user(form_data['name'])
                redirect = '/'
                flash = None

        return redirect, flash

    return  html.Div([
        html.Div([
            dhc.Redirect(id='signin-redirect', refresh=True),
            html.Div(className="col-md-2"),
            html.Div([
                html.Div([
                    html.Div([
                        html.Br(),
                        html.H4('Sign In'),
                        html.Br(),
                        dhc.Form(formFields(), id='form', preventDefault=True),
                        html.Br(),
                    ], className='card-body')
                ], className='card')
            ], className="col-md-8"),
            html.Div(className="col-md-2")
        ], className='row')
    ], className="container-fluid")


#
# python -m examples.form
#
# http://localhost:8050
#

if __name__ == '__main__':
    print('\nvisit: http://localhost:8050\n')

    aps_log = logging.getLogger('werkzeug')
    aps_log.setLevel(logging.ERROR)

    app.layout = layout
    app.run_server(debug=False, threaded=False)
