from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from decimal import Decimal
import Utilities.Logger as L

class BasePage:
    def __init__(self, driver, page_title):
        self.driver = driver
        self.page_title = page_title
        self.verify_page_title(page_title)

    def verify_page_title(self, page_title):
        is_title = WebDriverWait(self.driver, 30).until(EC.title_contains(page_title))
        if not is_title:
            L.logging.error(f'Navigation to page : {page_title} failed. Actual page title: {self.driver.title}')
            raise ValueError

    def hover_element(self, element):
        action = ActionChains(self.driver)
        action.move_to_element(element).perform()

    def click_element_with_actions(self, element):
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click().peform()

    def click_element(self, by_locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((by_locator))).click()

    def insert_text(self, element, text):
        element.click()
        element.clear()
        element.send_keys(text)

    def get_items_values_sum(self, items_list, split, index):
        sum = 0
        for item in items_list:
            if len(item.text) != 0:
                text = item.text.split(split, 1)[index]
                result = Decimal(text)
                sum += result
            else:
                L.logging.error("value can't be null or empty string")
                raise ValueError
        return sum

