from selenium.webdriver.chrome.options import Options
import logging
import pytest

from examples.form.index import create_app

# Turn off werkzeug logging as it's very noisy

aps_log = logging.getLogger('werkzeug')
aps_log.setLevel(logging.ERROR)


# This is needed to force Chrome to run without sandbox enabled. Docker
# does not support namespaces so running Chrome in a sandbox is not possible.
#
# See https://github.com/plotly/dash/issues/1420

def pytest_setup_options():
    options = Options()
    options.add_argument('--no-sandbox')
    return options

@pytest.fixture(scope='session')
def spa():
    """A Dash Application for the tests."""
    _spa = create_app()
    return _spa

@pytest.fixture(scope='function')
def duo(dash_duo, spa):
    """A client for the dash_duo/Flask tests."""
    dash_duo.start_server(spa, port=8051)
    return dash_duo
