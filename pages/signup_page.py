from playwright.sync_api import expect, Dialog
from time import sleep

class SignupPage:
    def __init__(self, page):
        self.page = page
        self.signup_link = page.locator("#signin2")
        self.username_input = page.locator("#sign-username")
        self.password_input = page.locator("#sign-password")
        self.signup_button = page.locator("button", has_text="Sign up")
        self.modal = page.locator("#signInModal")
        self.alert_message = None

    def handle_alert(self, dialog: Dialog):
        self.alert_message = dialog.message
        # print(f"Alert message: {dialog.message}")
        # print(self.alert_message)
        dialog.accept()

    def open_signup_modal(self):
        self.signup_link.click()
        expect(self.modal).to_be_visible()

    def signup(self, username, password):
        self.page.on("dialog", self.handle_alert)
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.signup_button.click()
        #print(f"Alert messag e again: {self.alert_message}")
        self.page.wait_for_timeout(3000) #we are waiting for the alert message to be processed, because if we do not wait the message will be None
        return self.alert_message
        

