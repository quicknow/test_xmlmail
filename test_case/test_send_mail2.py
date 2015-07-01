#coding=utf-8
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
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
    def test_send_mail4(self):
        driver = self.driver
        driver.get(self.base_url)
        #登录
        login.login(self,"zwbtestpython@126.com","zwb888888")
        #写信
        driver.find_element_by_xpath(".//*[@id='_mail_component_57_57']/span[2]").click()
        #填写收件人和主题
        driver.find_element_by_xpath("//*[@class='bz0']/div[2]/div/input").send_keys('testingwtb@126.com')
        time.sleep(2)
        #driver.find_element_by_xpath(".//*[@id='_mail_button_13_253']/span[2]").click()
        driver.find_element_by_xpath("//input[@class='nui-ipt-input' and @type='text' and @maxlength='256']").send_keys(u'给小明的信')
        
        #获得当前窗口的句柄
        window_handle = driver.window_handles
        
        #定位富文本表单
        print window_handle
        class_name = driver.find_element_by_class_name('APP-editor-iframe')
        driver.switch_to_frame(class_name)
        #编写邮件正文
        driver.find_element_by_tag_name('body').send_keys(u'你好，小明好久不见。')
        #退出iframe
        driver.switch_to_default_content()
        #driver.switch_to_window(window_handle)
        #断言发送结果
        #driver.find_element_by_xpath("//*[@id='_mail_button_11_237']/span[2]").click()
        
        driver.find_element_by_xpath("//header/div/div/div/span[2]").click()

        #需要一个加一个智能等待时间
        #time.sleep(2)
        #隐式等待
        #driver.implicitly_wait(6)
        
        #智能等待
        showelement=driver.find_element_by_class_name('tK1')
        
        element = WebDriverWait(driver,10,0.5).until(lambda driver : showelement.is_displayed())
     
        
        text = driver.find_element_by_class_name('tK1').text
        
        print text

        #断言验证
        self.assertEqual(text,u'发送成功免费短信通知')

        #退出
        login.logout(self)

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
if __name__ == "__main__":
    unittest.main()




