import time

import unittest
from selenium import webdriver

from Units import test_tools


class NovaBase(unittest.TestCase):
    # def __init__(self):
    #     super().__init__()
    #     self.u = test_tools.Unit()
    # instance = None
    #
    # def __new__(cls, *args, **kwargs):
    #     if cls.instance is None:
    #         cls.instance = super().__new__(cls)
    #     return cls.instance

    def setUp(self):
        '''前置条件:登录到系统的仪表盘界面'''
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("http://192.168.3.31/#/login")
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="test_username"]/div/div/input').send_keys("admin")
        self.driver.find_element_by_xpath('//*[@id="test_password"]/div/div/input').send_keys("admin")
        self.driver.find_element_by_xpath('//*[@id="test_password"]/div/div/div').click()
        time.sleep(2)

    def tearDown(self):
        self.driver.quit()
