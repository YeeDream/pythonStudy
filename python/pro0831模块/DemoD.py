# -*-coding:utf-8 -*-
# *-*Author:DreamYee*-*
# Create:2019/08/31 22:26
# File:DemoD.py

import os
print(dir(os))

# 操作文件：重命名  删除文件
'''
import os
os.rename("22201.py","newtemp.py")
'''
# 删除
'''
import os
os.remove("2.py")
'''
# 操作目录
'''
os.listdir:显示目录中的文件
os.getcwd, os.chdir:当前工作目录，改变当前工作目录
os.makedirs  os.removedirs:创建和删除目录
'''

# 文件和目录属性   os.stat()

import time
print(time.ctime())

import webbrowser
print(webbrowser.open("http://www.baidu.com"))