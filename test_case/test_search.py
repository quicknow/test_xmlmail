#coding=utf-8
from selenium import webdriver
import unittest, time
from public import login
import xml.dom.minidom
#打开xml 文档
dom = xml.dom.minidom.parse('D:\\pytest\\test_xmlmail\\test_data\\login.xml')
#得到文档元素对象
root = dom.documentElement
class TestSendMail(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        logins = root.getElementsByTagName('url')
        self.base_url=logins[0].firstChild.data
        self.verificationErrors = []

        #搜索邮件
    def test_search_mail(self):
        driver = self.driver
        driver.get(self.base_url)
        #调用登录模块
        login.login(self,'zwbtestpython@126.com','zwb888888')
        #搜索邮件
        driver.find_element_by_xpath("//input[@class='nui-ipt-input' and @type='text']").send_keys(u'小明')
        driver.find_element_by_xpath("//input[@class='nui-ipt-input' and @type='text']").send_keys(Keys.ENTER)
        #断言搜索邮件标签页面
        text= driver.find_element_by_xpath("//div[@id='dvMultiTab']/ul/li[5]/div[3]").text
        self.assertEqual(text,u'搜索邮件')
        #调用退出
        login.logout(self)

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
if __name__ == "__main__":
    unittest.main()

