from behave import given, when, then

@given('I am on the login page')
def steps_impl(context):
    context.login_page.open()

@when('Enter "{user}" in the username field')
def steps_impl(context, user):
    context.login_page.set_username(user)

@when('Enter "{password}" in the password field')
def steps_impl(context, password):
    context.login_page.set_password(password)

@when('Click the login button')
def steps_impl(context):
    context.login_page.click_login_button()

@then('I should see the "{title}" page title')
def steps_impl(context, title):
    context.products_page.verify_products_page_title(title)

@then('The url of the current page is "{url}"')
def steps_impl(context, url):
    context.products_page.verify_current_url(url)