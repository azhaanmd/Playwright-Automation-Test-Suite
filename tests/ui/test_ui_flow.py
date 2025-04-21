import pytest
from utils.data_loader import load_test_data
from pages.login_page import LoginPage
from pages.signup_page import SignupPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage
from pages.order_page import OrderPage
from playwright.sync_api import Playwright



test_data = load_test_data("test_data/ui_test_data.json")

@pytest.mark.parametrize("case", test_data["login"])
def test_login(playwright:Playwright, case):
    browser_context = playwright.chromium.launch(headless=True)
    page = browser_context.new_page()

    login = LoginPage(page)
    page.goto("https://demoblaze.com")

    login.open_login_modal()
    login.login(case["username"], case["password"])
    
    if case["expected"]:
        assert login.is_logged_in(), "Expected successful login"
        login.logout()
    else:
        assert not login.is_logged_in(), "Expected login failure"


def test_signup_new_and_duplicate(playwright:Playwright):
    browser_context = playwright.chromium.launch(headless=False)
    page = browser_context.new_page()
    signup = SignupPage(page)

    page.goto("https://demoblaze.com")
    # Test new user signup
    signup.open_signup_modal()
    signup.signup(
        test_data["signup"]["new_user"]["username"],
        test_data["signup"]["new_user"]["password"]
    )
    print("done")
    page.wait_for_timeout(3000)  # allow time for alert
    # Test duplicate user signup
    # signup.open_signup_modal()
    # message = signup.signup(
    #     test_data["signup"]["duplicate_user"]["username"],
    #     test_data["signup"]["duplicate_user"]["password"]
    # )
    # page.wait_for_timeout(3000)
    # print(message)


def test_add_and_remove_cart(browser_context):
    page = browser_context.new_page()
    login = LoginPage(page)
    product = ProductPage(page)
    cart = CartPage(page)

    page.goto("https://demoblaze.com")
    login.open_login_modal()
    login.login(test_data["login"][0]["username"], test_data["login"][0]["password"])

    product.select_product(test_data["product"]["name"])
    assert product.verify_product_loaded(test_data["product"]["name"])

    cart.add_to_cart()
    page.wait_for_timeout(2000)
    cart.go_to_cart()
    assert len(cart.get_cart_items()) > 0

    cart.delete_first_item()
    page.wait_for_timeout(2000)


def test_place_order(browser_context):
    page = browser_context.new_page()
    login = LoginPage(page)
    cart = CartPage(page)
    order = OrderPage(page)

    page.goto("https://demoblaze.com")
    login.open_login_modal()
    login.login(test_data["login"][0]["username"], test_data["login"][0]["password"])

    cart.go_to_cart()
    order.fill_order_form(test_data["order"])

    # Simple confirmation check
    assert page.locator("h2", has_text="Thank you for your purchase!").is_visible()


def test_logout(browser_context):
    page = browser_context.new_page()
    login = LoginPage(page)

    page.goto("https://demoblaze.com")
    login.open_login_modal()
    login.login(test_data["login"][0]["username"], test_data["login"][0]["password"])

    assert login.is_logged_in()
    login.logout()
    page.wait_for_timeout(1000)
