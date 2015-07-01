#coding=utf-8
import os
#定义文件目录
result_dir = 'D:\\pytest\\test_xmlmail\\report'
lists=os.listdir(result_dir)
print lists
print '\n'
#重新按时间对目录下的文件进行排列
lists.sort(key=lambda x: os.path.getmtime(result_dir+"\\"+x))
print ('最新的文件为： '+lists[-1])
file = os.path.join(result_dir,lists[-1])
print file
