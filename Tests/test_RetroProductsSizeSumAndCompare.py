from Tests.test_Base import TestBase
from Pages.HomePage import HomePage
import Utilities.Logger as L
import Utilities.Helper as H

class Test_RetroProductsSizeSumAndCompare(TestBase):

    size_to_compare = 4

    def test_retro_products_size_sum_compare(self):

        # open retro page
        home_page = HomePage(self.driver)
        retro_page = home_page.open_retro_page()

        # get all retro page products sum size
        sum_size = retro_page.get_product_size_sum()
        L.logging.info(f'Retro page products sum size: {sum_size}')

        # compare products sum size
        H.assert_test(sum_size > self.size_to_compare, f'Retro products size sum should be larger than: {self.size_to_compare}, '
                                                       f'actual size sum is: {sum_size}')