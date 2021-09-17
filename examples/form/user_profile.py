import dash
from dash.dependencies import Input, Output
from dash import html
import dash_holoniq_components as dhc

from app import app
from examples.form.common import big_center

NOUPDATE = dash.no_update

class UserProfile:

    def __init__(self):
        self.signout()

    def set_user(self, user):
        self.user = user

    def signout(self):
        self.user = 'Guest'

    def user_signed_in(self):
        return self.user != 'Guest'


user_profile = UserProfile()

# Define callbacks and return static content for the /user page

def layout():

    def profile_content():

        def sign_out_button():
            hidden = False if user_profile.user_signed_in() else True
            btn = html.Button('Sign out', id='signout-btn', className="btn btn-primary", hidden=hidden)
            return html.Div([btn], className="col text-center")

        return html.Header([
            big_center("Welcome"),
            big_center(user_profile.user, id='wellcome'),
            html.Br(),
            sign_out_button(),
        ], className='jumbotron my-4')

    user_content = html.Div(profile_content(), id='user_content')
    user_redirect =  dhc.Location(id='user_redirect', refresh=False)

    # Handle dynamic user specific content based on who's currently logged in

    @app.callback(Output('user_content', 'children'), [Input('loc','pathname')])
    def _content_callback(pathname):

        # This callback is triggered whenever the browser location changes, check that
        # it's the user page being displayed, if not return nothing

        return profile_content() if pathname == '/user' else NOUPDATE

    # User has clicked the sign out button

    @app.callback(Output('user_redirect', 'pathname'), [Input('signout-btn','n_clicks')])
    def _signout_btn_callback(n_clicks):
        redirect = NOUPDATE
        if n_clicks:
            user_profile.signout()
            redirect='/'

        return redirect

    # Return static layout

    return html.Header([user_redirect, user_content], className='jumbotron my-4')
