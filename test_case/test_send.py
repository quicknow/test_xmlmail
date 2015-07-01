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
#只填写收件人发送邮件
    def test_send_mail(self):
        driver = self.driver
        driver.get(self.base_url)
        #登录
        login.login(self,"zwbtestpython@126.com","zwb888888")
        #写信
        driver.find_element_by_xpath(".//*[@id='_mail_component_57_57']/span[2]").click() 
        #填写收件人
        driver.find_element_by_xpath("//*[@class='bz0']/div[2]/div/input").send_keys('testingwtb@126.com')
        #发送邮件
        driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/header/div/div/div/span[2]").click()
        driver.find_element_by_xpath("//*[@class='nui-msgbox-ft-btns']/div/span").click()
        #断言发送结果
        text = driver.find_element_by_class_name('tK1').text
        time.sleep(5)
        print text
        time.sleep(10)
        self.assertEqual(text,'F')
        login.logout(self)
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
if __name__ == "__main__":
    unittest.main()
