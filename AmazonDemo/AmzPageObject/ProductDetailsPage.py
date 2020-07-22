from AmazonDemo.TestBase.Setup import setupEnv
from selenium import webdriver
from selenium.webdriver.common.by import By
import logging

class ProductDetailPage(setupEnv):

    # Locator of Product Search Page
    productTitle = 'productTitle'
    productPrice = 'priceblock_ourprice'

    def getProductTitle(self):
        pdp = ProductDetailPage
        productTitle = self.driver.find_element_by_id(pdp.productTitle).text
        print('Product name on product details page ', productTitle)
        logging.info('Product name on product details page ', productTitle)
        return productTitle

    def getProductAmount(self):
        pdp = ProductDetailPage
        productAmt = self.driver.find_element_by_id(pdp.priceblock_ourprice).text
        return productAmt