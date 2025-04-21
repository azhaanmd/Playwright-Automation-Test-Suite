from playwright.sync_api import expect
from time import sleep
class LoginPage:
    def __init__(self, page):
        self.page = page
        self.login_link = page.locator("#login2")
        self.username_input = page.locator("#loginusername")
        self.password_input = page.locator("#loginpassword")
        self.login_button = page.locator("button", has_text="Log in")
        self.logout_link = page.locator("#logout2")
        self.modal = page.locator("#logInModal")

    def open_login_modal(self):
        self.login_link.click()
        expect(self.modal).to_be_visible()

    def login(self, username, password):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()


    def is_logged_in(self):
        try:
            expect(self.logout_link).to_be_visible(timeout=5000)
            return True
        except:
            return False

    def logout(self):
        self.logout_link.click()
