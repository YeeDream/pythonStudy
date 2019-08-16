# -*-coding:utf-8 -*-
# *-*Author:DreamYee*-*
# Create:2019/08/15 16:10
# File:DemoB文件.py

# 文件的状态
import os
file_stat = os.stat("E:\\upload\\131.txt")
print(file_stat)

import time
# 文件创建的时间
print(time.localtime(file_stat.st_ctime))

# read:如果指定了参数size，就按照该指定长度从文件中读取内容，否则，就读取全文。被读出来的内容，全部塞到一个字符串里面。
# readline:那个可选参数size的含义同上。
# 它则是以行为单位返回字符串，也就是每次读一行，依次循环，如果不限定size，直到最后一个返回的是空字符串，意味着到文件末尾了(EOF)。
# readlines:size同上。
# 它返回的是以行为单位的列表，即相当于先执行readline()，
#    得到每一行，然后把这一行的字符串作为列表中的元素塞到一个列表中，最后将此列表返回。
f = open("E:\\upload\\you.md")
# content = f.read()
content = f.readline()
for line in content:
    print(line, )
'''
# 读很大的文件：while循环和readline()
import fileinput
for line in fileinput.input("E:\\upload\\you.md")
    print(line, )
'''


# seek():让指针移动，以字节为单位移动
f = open("E:\\upload\\you.md")
f.readline()
f.seek(0)
print(f.readline())
print(f.tell())
