
from tests.form import USER_NAME, USER_PASSWORD

# Headless browser tests. Pytest setup, see tests/conftest.py, creates 
# an instance of examples/form. The following tests navigate 
# to a specific page and use the selenium driver to interact with th UI
#
# https://selenium-python.readthedocs.io/locating-elements.html

def test_default_page(duo):

    # Render default page

    duo.server_url = duo.server_url + "/"

    btn = duo.find_element("#signin")
    assert btn.text == "Sign In"

    btn.click()

    result = duo.wait_for_text_to_equal("#form_signin_btn", "Sign In", timeout=20)
    assert result

def test_form_submit_page(duo):

    # Open the sign in form

    duo.server_url = duo.server_url + "/signin"

    result = duo.wait_for_text_to_equal("#form_signin_btn", "Sign In", timeout=20)
    assert result

    # Enter user name & password

    name=duo.find_element("#user_name")
    name.send_keys(USER_NAME)

    password=duo.find_element("#password")
    password.send_keys(USER_PASSWORD)

    btn = duo.find_element("#form_signin_btn")
    btn.click()

    # Confirm redirect to the user profile page

    result = duo.wait_for_text_to_equal("#wellcome", USER_NAME, timeout=20)
    assert result

    # Return to the form page

    duo.driver.back()

    # Confirm that the form fields are clear

    assert duo.wait_for_text_to_equal("#user_name", "", timeout=20)
    assert duo.wait_for_text_to_equal("#password", "", timeout=20)
