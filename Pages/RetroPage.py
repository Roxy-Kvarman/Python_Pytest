from Pages.BasePage import BasePage
from Config.config import TestData

class RetroPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver, TestData.RETRO_PAGE_TITLE)

    def get_product_size_sum(self):
        sum = 0
        product_collection = self.driver.find_element_by_class_name("CollectionInner__Products")
        product_list = product_collection.find_elements_by_tag_name("h2")
        sum = self.get_items_values_sum(product_list, '"', 0)
        return sum
