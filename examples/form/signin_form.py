from utils import logging, log

import dash
from dash.dependencies import Input, Output

import dash_bootstrap_components as dbc
import dash_holoniq_components as dhc
from dash import html

from .common import form_container
from app import app

from .user_profile import user_profile

NOUPDATE = dash.no_update

"""
Shows the Alert, InputWithIcon, PasswordWithShow and Form components
"""
def formFields():
    return [
        dhc.Alert(id="flash", className="alert alert-danger", role="alert"),
        html.Div([
                dbc.Label("Name"),
                dhc.InputWithIcon(
                    value="",
                    type="name",
                    id="user_name",
                    name="name",
                    autoComplete="name",
                    placeholder="Enter name",
                    icon="fa fa-user",
                    tooltip="Hello Big Joe",
                ),
            ], className='mb-3'),
        html.Div([
                dbc.Label("Password"),
                dhc.PasswordWithShow(
                    value="",
                    name="password",
                    id="password",
                    autoComplete="password",
                    placeholder="Enter password",
                    tooltip="Hide/Show password",
                ),
            ], className='mb-3'),
        html.Div(
            html.Button("Sign In", id="form_signin_btn", type="submit", disabled=False, className="btn btn-primary btn-block"),
            className="form-group m-0",
        ),
    ]


def layout():

    # Process the user sign in form submit event

    @app.callback([Output("signin-redirect", "pathname"),
                   Output("form", "children"),
                   Output("flash", "children")],
                  [Input("form", "form_data")])
    def _callback(form_data):
        redirect = NOUPDATE
        form_fields = NOUPDATE
        flash = None


        if form_data:

            log.info("form data: %s", form_data)

            if form_data["name"] == "":
                flash = "Enter your name"
            elif len(form_data["password"]) < 8:
                flash = "Password must be at least 8 characters"
            else:

                # OK we have a valid user, save the profile

                user_profile.set_user(form_data["name"])

                # Clear any field errors that may have been flagged previously

                flash = None

                # Force a redirect to the user profile page

                redirect = "/user"

                # Reset the form fields. If we don't do this the
                # field content will be preserved in the DOM and will be
                # represented when the form is next shown. This may or may not
                # be desirable. If sensitive data fields a present in the form
                # then this will return them to the default values.

                form_fields = formFields()

        return redirect, form_fields, flash

    redirect = dhc.Location(id="signin-redirect", refresh=False)
    form = form_container("Sign In", formFields(), id="form")

    return html.Div([redirect, form])

#
# python -m examples.form.signin_form
#
# http://localhost:8050
#

if __name__ == "__main__":
    print("\nvisit: http://localhost:8050\n")

    aps_log = logging.getLogger("werkzeug")
    aps_log.setLevel(logging.ERROR)

    app.layout = layout()
    app.run_server(host='0.0.0.0', debug=False, threaded=False)
