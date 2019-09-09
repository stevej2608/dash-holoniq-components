import dash
from dash.dependencies import Input, Output
import dash_html_components as html
import dash_holoniq_components as dhc


from app import app

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


def big_center(text):
    return html.H2(text, className='display-3 text-center')

def layout():

    def signin():
        if user_profile.user == 'Guest':
            return html.Div([
                dhc.ButtonLink('Signin', href='/signin', className="btn btn-primary")
            ], className="col text-center")
        return None

    def signout():

        @app.callback(Output('signout-redirect', 'href'), [Input('signout-btn','n_clicks')])
        def _signout_callback(clicks):
            redirect = NOUPDATE
            if clicks:
                user_profile.signout()
                redirect = '/'

            return redirect


        if user_profile.user != 'Guest':
            return html.Div([
                dhc.Redirect(id='signout-redirect', refresh=True),
                html.Button('Signout', id='signout-btn', className="btn btn-primary")
            ], className="col text-center")
        return None


    return html.Header([
        big_center("Welcome"),
        big_center(user_profile.user),
        html.Br(),
        signin(),
        signout()
    ], className='jumbotron my-4')