import unittest
from selenium import webdriver
import logging
from configparser import ConfigParser


class setupEnv(unittest.TestCase):

    file ='C:\\Users\\Zeeshan_Ali\\PycharmProjects\\SeleniumPython\\AmazonDemo\\config.ini'
    config = ConfigParser()
    config.read(file)

    def setUp(self):
        setup = setupEnv
        print("--------------------------------------------------")
        print("Test case sarted")
        self.driver = webdriver.Chrome(executable_path=setup.config['EnvVar']['path'])
        print('Chrome browser launching')
        self.driver.get(setup.config['EnvVar']['url'])
        print('Navigated to ',setup.config['EnvVar']['url'])
        self.driver.implicitly_wait(20)
        self.driver.maximize_window()


    def tearDown(self):
        print('Test execution completed')
        self.driver.close()
        self.driver.quit()

    def logger_Config(self):
        s = setupEnv
        logging.basicConfig(filename=s.logFilePath,
                            format=' %(asctime) s: %(lavelname)s: %(message)s',
                            lavel=logging.DEBUG)


