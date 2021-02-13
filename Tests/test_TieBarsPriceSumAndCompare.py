from Tests.test_Base import TestBase
from Pages.HomePage import HomePage
import Utilities.Logger as L
import Utilities.Helper as H

class Test_TieBarsPriceSumAndCompare(TestBase):

    price_to_compare = 20

    def test_tie_bars_price_size_sum_compare(self):

        # open tie bars page
        home_page = HomePage(self.driver)
        tie_bars_page = home_page.open_tie_bars_page()

        # get all tie bars products price sum
        sum_price = tie_bars_page.get_tie_bars_price_sum()
        L.logging.info(f'Tie Bars price sum is: {sum_price}')

        # compare products sum price
        H.assert_test(sum_price < self.price_to_compare,
                    f'Tie Bars price sum should be higher than: {self.price_to_compare}, actual price sum is: {sum_price}')



