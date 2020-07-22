from AmazonDemo.TestBase.Setup import setupEnv
from selenium import webdriver
from selenium.webdriver.common.by import By
import logging

class ProductSearchPage(setupEnv):

    #Locator of Product Search Page
    first_SearchProduct = "//div[@class = 's-main-slot s-result-list s-search-results sg-row']/div[1]/div/span/div/div/div[2]//a/span"

    def getProductNameFromSearchedProduct(self):
        psp = ProductSearchPage
        productName = self.driver.find_element_by_xpath(psp.first_SearchProduct).text
        print('Product name on search product page ', productName)
        logging.info('Product name on search product page ', productName)
        return productName

    def clickOnProduct(self):
        psp = ProductSearchPage
        self.driver.find_element_by_xpath(psp.first_SearchProduct).click()
        print('user able to click on product')
        logging.info('user able to click on product')

