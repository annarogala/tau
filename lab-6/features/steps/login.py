from selenium import webdriver
from selenium.webdriver.common.by import By
from behave import given, when, then


INVALID_USERNAME_ERROR_MESSAGE = "Your username is invalid!"
INVALIV_PASSWORD_ERROR_MESSAGE = "Your password is invalid!"

@given("Firefox browser opened")
def step_open_browser(context):
    context.driver = webdriver.Firefox()
    context.driver.implicitly_wait(5)

@given("Chrome browser opened")
def step_open_browser(context):
    context.driver = webdriver.Chrome()
    context.driver.implicitly_wait(5)

@given("Wait '{seconds_number}' seconds")
def step_impl(context, seconds_number):
    context.driver.implicitly_wait(seconds_number)

@when("navigate to '{url}'")
def step_navigate_to_url(context, url):
    context.driver.get(url)

@when("enter login '{username}'")
def step_enter_username(context, username):
    username_field = context.driver.find_element(By.ID, "username")
    username_field.send_keys(username)

@when("enter password '{password}'")
def step_enter_password(context, password):
    password_field = context.driver.find_element(By.ID, "password")
    password_field.send_keys(password)

@when("click submit button")
def step_click_submit(context):
    submit_button = context.driver.find_element(By.ID, "submit")
    submit_button.click()

@then(u'redirect to \'{url}\'')
def step_impl(context, url):
    expected_url = url
    current_url = context.driver.current_url
    assert url == context.driver.current_url, f'Expected url to be {expected_url} but was {current_url}'

@then('successfully logged in message is displayed')
def step_impl(context):
    bodyText = context.driver.find_element(By.CLASS_NAME, "page").text
    assert "Congratulations" in bodyText or "successfully logged in" in bodyText, f"Expected 'Congratulations' or 'successfully logged in' but got '{bodyText}'"

@then("wrong username error message is displayed")
def step_verify_error_message(context):
    error_text = context.driver.find_element(By.ID, "error").text
    assert INVALID_USERNAME_ERROR_MESSAGE == error_text, f"Expected '{INVALID_USERNAME_ERROR_MESSAGE}' but got '{error_text}'"

@then("wrong password error message is displayed")
def step_verify_error_message(context):
    error_text = context.driver.find_element(By.ID, "error").text
    assert INVALIV_PASSWORD_ERROR_MESSAGE == error_text, f"Expected '{INVALIV_PASSWORD_ERROR_MESSAGE}' but got '{error_text}'"

@then("browser is closed")
def step_close_browser(context):
    context.driver.quit()