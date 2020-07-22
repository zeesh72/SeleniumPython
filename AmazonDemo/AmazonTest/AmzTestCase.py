from AmazonDemo.TestBase.Setup import setupEnv
from AmazonDemo.AmzPageObject.HomePage import HomePage
from AmazonDemo.AmzPageObject.ProductSearchPage import ProductSearchPage
from AmazonDemo.AmzPageObject.ProductDetailsPage import ProductDetailPage
import logging

import unittest

class AmzTestDemo(setupEnv,unittest.TestCase):

    def test_VerifySearchProductUsingSearchBox(self):
        home = HomePage
        title = self.driver.title
        print('the title' ,title)
        self.assertEqual(home.pagetitle,title,"landed page is not 'Amazon.in'")
        home.enterProductNameInSearchBox(self)
        home.clickOnSearchButton(self)

    def test_VerifyFirstSearchResult(self):
        home = HomePage
        psp = ProductSearchPage
        home.enterProductNameInSearchBox(self)
        home.clickOnSearchButton(self)
        productName = psp.getProductNameFromSearchedProduct(self)
        self.assertEqual(home.search_Product,productName,"Seached product is not correct")

    def test_VerifyProductDetails(self):
        home = HomePage
        psp = ProductSearchPage
        pdp = ProductDetailPage
        home.enterProductNameInSearchBox(self)
        home.clickOnSearchButton(self)
        psp.clickOnProduct(self)
        window = self.driver.window_handles[1]
        self.driver.switch_to_window(window)
        prodTitle = pdp.getProductTitle(self)
        print(prodTitle)
        self.assertEqual(home.search_Product,prodTitle,'product details page is not correct')








if __name__ == "__main__":
    unittest.main()






