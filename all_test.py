#coding=utf-8
import unittest
import HTMLTestRunner
import time
def creatsuite():
    testunit=unittest.TestSuite()
    #定义测试文件查找的目录
    test_dir='D:\\pytest\\test_xmlmail\\test_case'
    #定义discover 方法的参数
    discover=unittest.defaultTestLoader.discover(test_dir,pattern='test*.py',top_level_dir=None)
    #discover 方法筛选出来的用例，循环添加到测试套件中
    for test_case in discover:
        print test_case
        testunit.addTests(test_case)
    return testunit
now = time.strftime("%Y-%m-%d %H_%M_%S")
filename = 'D:\\pytest\\test_xmlmail\\report\\'+now+'result.html'
fp = file(filename, 'wb')
runner=HTMLTestRunner.HTMLTestRunner(stream=fp,title=u'百度搜索测试报告',description=u'用例执行情况：')
if __name__ == '__main__':
    alltestnames = creatsuite()
    runner.run(alltestnames)
    fp.close()
