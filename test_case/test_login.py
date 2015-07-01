#coding=utf-8
from selenium import webdriver
import unittest, time
from public import login
import xml.dom.minidom
#打开xml 文档
dom = xml.dom.minidom.parse('D:\\pytest\\test_xmlmail\\test_data\\login.xml')
#得到文档元素对象
root = dom.documentElement
class TestLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        logins = root.getElementsByTagName('url')
        self.base_url=logins[0].firstChild.data
        self.verificationErrors = []
    #用户名、密码为空
    def test_null(self):
        driver = self.driver
        driver.get(self.base_url)
        logins = root.getElementsByTagName('null')
        #获得null 标签的username、passwrod 属性值
        username=logins[0].getAttribute("username")
        password=logins[0].getAttribute("password")
        prompt_info = logins[0].firstChild.data
        #登录
        login.login(self,username,password)
        #获取断言信息进行断言
        text = driver.find_element_by_xpath("//div[@class='error-tt']/p").text
        self.assertEqual(text,prompt_info)
    #输入用户名、密码为空
    def test_pawd_null(self):
        driver = self.driver
        driver.get(self.base_url)
        logins = root.getElementsByTagName('pawd_null')
        #获得null 标签的username、passwrod 属性值
        username=logins[0].getAttribute("username")
        password=logins[0].getAttribute("password")
        prompt_info = logins[0].firstChild.data
        #登录
        login.login(self,username,password)
        #获取断言信息进行断言
        text = driver.find_element_by_xpath("//div[@class='error-tt']/p").text
        self.assertEqual(text,prompt_info)
    #用户名为空，只输入密码
    def test_user_null(self):
        driver = self.driver
        driver.get(self.base_url)
        logins = root.getElementsByTagName('user_null')
        #获得null 标签的username、passwrod 属性值
        username=logins[0].getAttribute("username")
        password=logins[0].getAttribute("password")
        prompt_info = logins[0].firstChild.data
        #登录
        login.login(self,username,password)
        #获取断言信息进行断言

        time.sleep(10)
        text = driver.find_element_by_xpath(".//*[@id='bubbleLayerWrap']/div/p").text
        self.assertEqual(text,prompt_info)
        #用户名密码错误
    def test_error(self):
        driver = self.driver
        driver.get(self.base_url)
        logins = root.getElementsByTagName('error')
        #获得null 标签的username、passwrod 属性值
        username=logins[0].getAttribute("username")
        password=logins[0].getAttribute("password")
        prompt_info = logins[0].firstChild.data
        #登录
        login.login(self,username,password)
        #获取断言信息进行断言
        text = driver.find_element_by_xpath("//div[@class='error-tt']/p").text
        self.assertEqual(text,prompt_info)
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
if __name__ == "__main__":
    unittest.main()
