import unittest
from appium import webdriver
import sys
from os.path import dirname, abspath
import app_config
BASE_PATH = dirname(dirname(abspath(__file__)))
sys.path.append(BASE_PATH)


class MyTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", options=app_config.options)
        cls.driver.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


