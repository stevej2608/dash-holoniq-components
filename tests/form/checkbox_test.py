from tests.form import USER_NAME, USER_PASSWORD

# Headless browser tests. Pytest setup, see tests/conftest.py, creates 
# an instance of examples/form. The following tests navigate 
# to a specific page and use the selenium driver to interact with th UI
#
# https://selenium-python.readthedocs.io/locating-elements.html

def test_form_checkbox(duo):

    def get_form_data():

        btn = duo.find_element("#form_submit")
        btn.click()

        report = duo.find_element("#report")
        return report.text

    # Open the sign in form

    duo.server_url = duo.server_url + "/checkbox"

    # Test initial data

    form_data = get_form_data()
    assert form_data == '{ "form_data": { "chk1": true, "chk2": false, "opt3": false, "radio-item": "1", "tog1": true, "tog2": false, "toggle3": false } }'

    # Test radio button # 1

    btn = duo.find_element("#rad1")
    btn.click()
    form_data = get_form_data()
    assert form_data == '{ "form_data": { "chk1": true, "chk2": false, "opt3": false, "radio-item": "1", "tog1": true, "tog2": false, "toggle3": false } }'

    # Test radio button # 2

    btn = duo.find_element("#rad2")
    btn.click()
    form_data = get_form_data()
    assert form_data == '{ "form_data": { "chk1": true, "chk2": false, "opt3": false, "radio-item": "2", "tog1": true, "tog2": false, "toggle3": false } }'

    # Test check box 1

    btn = duo.find_element("#chk1")
    btn.click()
    form_data = get_form_data()
    assert form_data == '{ "form_data": { "chk1": false, "chk2": false, "opt3": false, "radio-item": "2", "tog1": true, "tog2": false, "toggle3": false } }'

    # Test check box 2

    btn = duo.find_element("#chk2")
    btn.click()
    form_data = get_form_data()
    assert form_data == '{ "form_data": { "chk1": false, "chk2": true, "opt3": false, "radio-item": "2", "tog1": true, "tog2": false, "toggle3": false } }'

    # Test check toggle 1

    btn = duo.find_element("#tog1")
    btn.click()
    form_data = get_form_data()
    assert form_data == '{ "form_data": { "chk1": false, "chk2": true, "opt3": false, "radio-item": "2", "tog1": false, "tog2": false, "toggle3": false } }'

    # Test check toggle 2

    btn = duo.find_element("#tog2")
    btn.click()
    form_data = get_form_data()
    assert form_data == '{ "form_data": { "chk1": false, "chk2": true, "opt3": false, "radio-item": "2", "tog1": false, "tog2": true, "toggle3": false } }'
