# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re


def login(self,username,password):
        driver = self.driver
        driver.find_element_by_id("idInput").clear()
        driver.find_element_by_id("idInput").send_keys(username)
        driver.find_element_by_id("pwdInput").clear()
        driver.find_element_by_id("pwdInput").send_keys(password)
        driver.find_element_by_id("loginBtn").click()
        

def logout(self):
        driver = self.driver
        driver.find_element_by_link_text(u"退出").click()


if __name__ == "__main__":
    unittest.main()
