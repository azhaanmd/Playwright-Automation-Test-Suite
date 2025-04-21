class ProductPage:
    def __init__(self, page):
        self.page = page

    def select_product(self, name):
        self.page.click(f"text={name}")

    def verify_product_loaded(self, name):
        return name in self.page.inner_text(".name")
