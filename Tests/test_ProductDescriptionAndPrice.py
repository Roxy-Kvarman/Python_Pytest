from Tests.test_Base import TestBase
from Pages.HomePage import HomePage
import Utilities.Logger as L
import Utilities.Helper as H


class Test_ProductDescriptionAndPrice(TestBase):
    
    product_name = "Black Poplin Skinny Tie"
    price_to_compare = 10

    def test_get_product_description_and_compare_price(self):

        # open product page
        home_page = HomePage(self.driver)
        product_page = home_page.open_product_page(self.product_name)

        # get product description and price
        description = product_page.description
        price = product_page.price

        L.logging.info(f'Product: {self.product_name} - description: {description}')
        L.logging.info(f'Product: {self.product_name} - price: {price}')

        # compare product price
        is_price, product_price = product_page.price_compare(price, self.price_to_compare)

        # assert
        H.assert_test(is_price, f'Product: {self.product_name} price should be higher than {str(self.price_to_compare)}, '
                                f'actual price is:{product_price}')

