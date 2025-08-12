import unittest
import sys
from os.path import dirname, abspath
from common.my_test import MyTest
from page.login_page import LoginPage
BASE_PATH = dirname(dirname(abspath(__file__)))
sys.path.append(BASE_PATH)


class TestLogin(MyTest):

    def test_login(self):
        '''登录测试-正确用户名'''
        print("登录测试-正确用户名")
        login_page = LoginPage(self.driver)
        login_page.username.send_keys("13258861627")
        login_page.password.send_keys("123456")
        login_page.login_button.click()


if __name__ == '__main__':
    unittest.main()