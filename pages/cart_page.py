from playwright.sync_api import expect
from time import sleep

class CartPage:
    def __init__(self, page):
        self.page = page

    def add_to_cart(self):
        self.page.locator("a", has_text="Add to cart").click()
        self.page.on("dialog", lambda dialog: dialog.accept())

    def go_to_cart(self):
        self.page.locator("#cartur").click()

    def get_cart_items(self):
        return self.page.locator("tr.success").all()

        
    def delete_first_item(self):
        rows = self.page.locator("tr.success").all()
        for row in rows:
            print(row.text_content())

        print(self.page.locator("tr.success").nth(0).text_content())
        self.page.locator("tr.success").nth(0).locator("a", has_text="Delete").click()




