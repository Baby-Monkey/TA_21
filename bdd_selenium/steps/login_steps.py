from behave import given, when, then

from pages.login_page import LoginPage


@given("I am on the login page")
def steps_impl(context):
    context.login_page.open()

@when('I enter "{text}" in the email field')
def steps_impl(context, text):
    context.login_page.set_email(text)

@when('I enter "{text}" in the password field')
def steps_impl(context, text):
    context.login_page.set_password(text)

@when('I click the login button')
def steps_impl(context):
    context.login_page.click_login()

@then('I should see "{text}" message')
def steps_impl(context, text):
    context.login_page.verify_error_message(text)

@then('I should see the Logout button')
def step_impl(context):
    context.login_page.verify_logout_button_present()

@then('I should see the MyAccout button')
def step_impl(context):
    context.login_page.verify_myaccount_button_present()
