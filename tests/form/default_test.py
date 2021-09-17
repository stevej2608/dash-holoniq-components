
from tests.form import USER_NAME, USER_PASSWORD

def test_default_page(duo):

    # Render default page

    duo.server_url = duo.server_url + "/"

    btn = duo.find_element("#signin")
    assert btn.text == "Sign In"

    btn.click()

    result = duo.wait_for_text_to_equal("#form_signin_btn", "Sign In", timeout=20)
    assert result

def test_form_submit_page(duo):
    duo.server_url = duo.server_url + "/signin"

    result = duo.wait_for_text_to_equal("#form_signin_btn", "Sign In", timeout=20)
    assert result

    name=duo.find_element("#user_name")
    name.send_keys(USER_NAME)

    password=duo.find_element("#password")
    password.send_keys(USER_PASSWORD)

    btn = duo.find_element("#form_signin_btn")
    btn.click()

    result = duo.wait_for_text_to_equal("#signout-btn", "Sign out", timeout=20)
    assert result
