from browser import Browser
from pages.base_page import BasePage
from pages.login_page import LoginPage
from pages.products_page import ProductsPage


def before_all(context):
    context.browser = Browser()
    context.base_page = BasePage()
    context.login_page = LoginPage()
    context.products_page = ProductsPage()

def after_all(context):
    context.browser.close()