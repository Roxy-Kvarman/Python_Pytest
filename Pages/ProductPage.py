from Pages.BasePage import BasePage
from Config.config import TestData

class ProductPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver, TestData.PRODUCT_PAGE_TITLE)

    @property
    def description(self):
        description = self.get_item_info("ProductMeta__Description")
        description = description.split(".", 1)[0]
        return description

    @property
    def price(self):
        price = self.get_item_info("ProductMeta__PriceList")
        price = price.replace("$", "")
        return price

    def price_compare(self, price, price_to_compare):
        product_price = int(price)
        is_price = product_price > price_to_compare
        return is_price, product_price

    def get_item_info(self, locator):
        item_info = self.driver.find_element_by_class_name(locator)
        text = item_info.text
        return text
