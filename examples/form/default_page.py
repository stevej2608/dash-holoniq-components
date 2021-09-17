from dash import dcc, html

from examples.form.common import big_center

# Default static page, displayed when the url path is not valid

def layout():

    def signin():
        return html.Div([
            dcc.Link('Sign In', id='signin', href='/signin', className="btn btn-primary", refresh=False)
        ], className="col text-center")

    return html.Header([
        big_center("Welcome To"),
        big_center("Dash Holoniq Components"),
        html.Br(),
        signin()
    ], className='jumbotron my-4')
