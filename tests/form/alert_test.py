
from tests.form import USER_NAME, USER_PASSWORD

# Headless browser tests. Pytest setup, see tests/conftest.py, creates 
# an instance of examples/form. The following tests navigate 
# to a specific page and use the selenium driver to interact with th UI
#
# https://selenium-python.readthedocs.io/locating-elements.html


def test_alert_component(duo):

    # Open the sign in form

    duo.server_url = duo.server_url + "/signin"

    # Try to submit empty form

    btn = duo.find_element("#form_signin_btn")
    btn.click()

    assert duo.wait_for_text_to_equal("#flash", "Enter your name", timeout=20)

    # Try to submit user name with no password

    name=duo.find_element("#user_name")
    name.send_keys(USER_NAME)

    btn.click()

    assert duo.wait_for_text_to_equal("#flash", "Password must be at least 8 characters", timeout=20)
