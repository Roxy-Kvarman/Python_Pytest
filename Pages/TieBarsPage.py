from Pages.BasePage import BasePage
from Config.config import TestData
import time


class TieBarsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver, TestData.TIE_BARS_PAGE_TITLE)

    def get_tie_bars_price_sum(self):
        self.driver.execute_script("window.scrollBy(0,900)")
        time.sleep(5)
        product_collection = self.driver.find_element_by_class_name("CollectionInner__Products")
        product_list = product_collection.find_elements_by_class_name("ProductItem__PriceList")
        sum = self.get_items_values_sum(product_list, "$", -1)
        return sum





