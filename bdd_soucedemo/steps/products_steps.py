from behave import given, when, then

@given('I am on the products page as standard user')
def step_impl(context):
    context.login_page.login("standard_user", "secret_sauce")

@then('Products names are sorted alphabetically')
def step_impl(context):
    context.products_page.verify_product_names_sorted_alphabetically()

@when('I sort the products "{text}"')
def step_impl(context, text):
    context.products_page.select_dropdown_item(text)

@then('Products are sorted by price from low to high')
def step_impl(context):
    context.products_page.verify_product_price_sorted_low_to_high()

@when('I click the add to cart button')
def step_impl(context):
    context.products_page.click_add_backpack_button()

@then('The button name chage to Remove')
def step_impl(context):
    context.products_page.verify_remove_button_is_visible()

@then('Item number "{number}" is displayed on the cart')
def step_impl(context, number):
    context.products_page.verify_cart_item_number(number)