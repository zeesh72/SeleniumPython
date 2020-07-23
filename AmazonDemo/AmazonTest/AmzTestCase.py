from AmazonDemo.TestBase.Setup import setupEnv
from AmazonDemo.AmzPageObject.HomePage import HomePage
from AmazonDemo.AmzPageObject.ProductSearchPage import ProductSearchPage
from AmazonDemo.AmzPageObject.ProductDetailsPage import ProductDetailPage
import logging

import unittest

class AmzTestDemo(setupEnv,unittest.TestCase):

    def test_VerifySearchProductUsingSearchBox(self):
        home = HomePage
        setup = setupEnv
        title = self.driver.title
        print('the title' ,title)
        self.assertEqual(setup.config['TestData']['pagetitle'],title,"landed page is not 'Amazon.in'")
        home.enterProductNameInSearchBox(self)
        home.clickOnSearchButton(self)

    def test_VerifyFirstSearchResult(self):
        home = HomePage
        setup = setupEnv
        psp = ProductSearchPage
        home.enterProductNameInSearchBox(self)
        home.clickOnSearchButton(self)
        productName = psp.getProductNameFromSearchedProduct(self)
        self.assertEqual(setup.config['TestData']['search_Product'],productName,'Seached product is not correct')
        print('The first item on Seached product list is',setup.config['TestData']['search_Product'])

    def test_VerifyProductDetails(self):
        home = HomePage
        setup = setupEnv
        psp = ProductSearchPage
        pdp = ProductDetailPage
        home.enterProductNameInSearchBox(self)
        home.clickOnSearchButton(self)
        psp.clickOnProduct(self)
        window = self.driver.window_handles[1]
        self.driver.switch_to_window(window)
        prodTitle = pdp.getProductTitle(self)
        print(prodTitle)
        self.assertEqual(setup.config['TestData']['search_Product'],prodTitle,'product details page is not correct')
        print('After clicking on the product, product details page opened with product title as',setup.config['TestData']['search_Product'])








