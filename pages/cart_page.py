from playwright.sync_api import expect

class CartPage:
    def __init__(self, page):
        self.page = page

    def add_to_cart(self):
        self.page.click("a", has_text="Add to cart")
        self.page.on("dialog", lambda dialog: dialog.accept())

    def go_to_cart(self):
        self.page.click("#cartur")

    def get_cart_items(self):
        return self.page.locator("tr.success").all()

    def delete_first_item(self):
        self.page.click("a", has_text="Delete")
