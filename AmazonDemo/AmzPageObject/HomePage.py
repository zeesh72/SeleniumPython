from AmazonDemo.TestBase.Setup import setupEnv
from selenium import webdriver
from selenium.webdriver.common.by import By
import logging

class HomePage(setupEnv):

    #Locator of Home Page
    txt_SearchBox = 'twotabsearchtextbox'
    btn_Search = "//input[@type='submit']"

    #Test Data
    search_Product = 'OnePlus 8 (Glacial Green 6GB RAM+128GB Storage)'
    pagetitle = 'Online Shopping site in India: Shop Online for Mobiles, Books, Watches, Shoes and More - Amazon.in'

    def getPageTitle(self):
        title=self.driver.title

    def enterProductNameInSearchBox(self):
        home = HomePage
        self.driver.find_element_by_id(home.txt_SearchBox).clear()
        self.driver.find_element_by_id(home.txt_SearchBox).send_keys(home.search_Product)
        print('user able to enter search product in search box')
        logging.info('user able to enter search product in search box')

    def clickOnSearchButton(self):
        home = HomePage
        self.driver.find_element_by_xpath(home.btn_Search).click()
        print('user able to click om search icon')
        logging.info('user able to click om search icon')










