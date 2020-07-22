import unittest
from selenium import webdriver
import logging


class setupEnv(unittest.TestCase):

    path = "C:\\Users\\Zeeshan_Ali\\Downloads\\chromedriver_win32 (2)\\chromedriver.exe"
    url = "https://www.amazon.in/"
    logFilePath = "C://Users//Zeeshan_Ali//PycharmProjects//SeleniumPython//AmazonDemo//LogFiles//log.txt"


    def setUp(self):
        s = setupEnv
        self.driver = webdriver.Chrome(executable_path=s.path)
        print('Chrome browser launching')
        self.driver.get(s.url)
        print('Navigating to ',s.url)
        self.driver.implicitly_wait(20)
        self.driver.maximize_window()

    def tearDown(self):
        print('Test execution completed')
        self.driver.close()
        self.driver.quit()

    def log_Config(self):
        s = setupEnv
        logging.basicConfig(filename=s.logFilePath,
                            format=' %(asctime) s: %(lavelname)s: %(message)s',
                            lavel=logging.DEBUG)


