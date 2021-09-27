import os
from utils import logging, log
import dash
import dash_bootstrap_components as dbc

app = dash.Dash(__name__,
                suppress_callback_exceptions=True,
                external_stylesheets=[
                    dbc.themes.BOOTSTRAP,
                    'https://stackpath.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css'
                ])

app.scripts.config.serve_locally = True
app.css.config.serve_locally = True


def serve_app(app, path="", debug=False):

    # Turn off werkzeug  logging as it's very noisy

    aps_log = logging.getLogger('werkzeug')
    aps_log.setLevel(logging.ERROR)

    # Set SPA logging level (if needed)

    log.setLevel(logging.INFO)

    # When running in a Docker container the internal port
    # is mapped onto a host port. Use the env variables passed
    # in to the container to determin the host URL.

    port = int(os.environ.get("PORT", 8060))
    hostname = os.environ.get("HOST_HOSTNAME", "localhost")
    hostport = os.environ.get("HOST_HOSTPORT", "8050")

    print(f' * Visit http://{hostname}:{hostport}{path}')

    app.run_server(debug=debug, host='0.0.0.0', port=port, threaded=False, dev_tools_serve_dev_bundles=True)
