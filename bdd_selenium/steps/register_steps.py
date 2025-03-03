from behave import given, when, then

@given('I am on the register page')
def step_impl(context):
    context.register_page.open()

@when('I enter "{first_name}" in first name input field')
def step_impl(context, first_name):
    context.register_page.type_first_name(first_name)

@when('I enter "{last_name}" in last name input field')
def step_impl(context,last_name):
    context.register_page.type_last_name(last_name)

@when('I enter "{email}" in email input field')
def step_impl(context, email):
    context.register_page.type_email(email)

@when('I enter "{password}" in password input field')
def step_impl(context, password):
    context.register_page.type_password(password)

@when('I enter "{confirm_password}" in confirm password input field')
def step_impl(context, confirm_password):
    context.register_page.type_confirm_password(confirm_password)

@when('I click the register button')
def step_impl(context):
    context.register_page.click_register_button()

@then('I should see "{text}" register message')
def step_impl(context, text):
    context.register_page.verify_register_message(text)