from playwright.sync_api import expect
from time import sleep


class SignupPage:
    def __init__(self, page):
        self.page = page
        self.signup_link = page.locator("#signin2")
        self.username_input = page.locator("#sign-username")
        self.password_input = page.locator("#sign-password")
        self.signup_button = page.locator("button", has_text="Sign up")
        self.modal = page.locator("#signInModal")

    def open_signup_modal(self):
        self.signup_link.click()
        expect(self.modal).to_be_visible()

    def signup(self, username, password):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.page.on("dialog", lambda dialog:print(dialog.message))
        self.signup_button.click()
        

