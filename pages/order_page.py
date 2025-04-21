from playwright.sync_api import expect

class OrderPage:
    def __init__(self, page):
        self.page = page
        self.place_order_btn = page.locator("button", has_text="Place Order")
        self.modal = page.locator("#orderModal")
        self.name = page.locator("#name")
        self.country = page.locator("#country")
        self.city = page.locator("#city")
        self.card = page.locator("#card")
        self.month = page.locator("#month")
        self.year = page.locator("#year")
        self.purchase_btn = page.locator("button", has_text="Purchase")

    def fill_order_form(self, order_info):
        self.place_order_btn.click()
        expect(self.modal).to_be_visible()
        self.name.fill(order_info["name"])
        self.country.fill(order_info["country"])
        self.city.fill(order_info["city"])
        self.card.fill(order_info["card"])
        self.month.fill(order_info["month"])
        self.year.fill(order_info["year"])
        self.purchase_btn.click()
