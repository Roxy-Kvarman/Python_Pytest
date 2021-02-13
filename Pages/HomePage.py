from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from Pages.BasePage import BasePage
from Pages.ProductPage import ProductPage
from Pages.RetroPage import RetroPage
from Pages.TieBarsPage import TieBarsPage
from Config.config import TestData
import Utilities.Logger as L
import time

class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver, TestData.HOME_PAGE_TITLE)

    def open_product_page(self, product_name):
        L.logging.info("Open Product Page")
        self.click_element((By.XPATH, "//a[text()='Search']"))
        self.__input_text_to_search__(product_name)
        self.click_element((By.XPATH, ("//img[contains(@alt,'" + product_name + "')]")))
        return ProductPage(self.driver)

    def open_retro_page(self):
        L.logging.info("Open Retro Page")
        pattern_btn = self.driver.find_element(By.XPATH, "//a[text()='Pattern']")
        self.hover_element(pattern_btn)
        time.sleep(5)
        options = pattern_btn.find_elements(By.XPATH, "..//ul/li")
        option_retro = next((x for x in options if x.text == "Retro"), None)
        option_retro.click()
        return RetroPage(self.driver)

    def open_tie_bars_page(self):
        L.logging.info("Open Tie Bars Page")
        tie_bars_links = self.driver.find_elements(By.XPATH, "//a[text()='Tie Bars']")
        tie_bar_link = next((link for link in tie_bars_links if link.is_displayed() and link.is_enabled()),None)
        tie_bar_link.click()
        return TieBarsPage(self.driver)
        
    def __input_text_to_search__(self, text):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, "Search")))
        search = self.driver.find_element(By.ID, "Search")
        input_field = search.find_element(By.TAG_NAME, "input")
        self.insert_text(input_field, text)
