# -*-coding:utf-8 -*-
# *-*Author:DreamYee*-*
# Create:2019/08/15 15:46
# File:DemoA文件.py

# 打开文件
f = open("E:\\upload\\130.txt")
for line in f:
    print(line,)

# 创建文件
nf = open("E:\\upload\\131.txt", "w")
nf.write("This is a file")

'''
模式          描述
r         以读方式打开文件，可读取文件信息
w         以写方式打开文件，可向文件写入信息。如文件存在，则清空该文件，再写入新内容
a         以追加模式打开文件（即一打开文件，文件指针自动移到文件末尾），如果文件不存在则创建
r+        以读写方式打开文件，可对文件进行读和写操作
w+        消除文件内容，然后以读写方式打开文件
a+        以读写方式打开文件，并把文件指针移到文件尾
b         以二进制模式打开文件，而不是以文本模式。
'''
fp = open("E:\\upload\\131.txt")
for line in fp:
    print(line)
fp = open("E:\\upload\\131.txt", "w")
fp.write("My name is dream.My website is dream.github.io")

fp = open("E:\\upload\\131.txt", "a")
fp.write("\nAna ,I like program\n")
fp.close() # 关闭文件，一定要养成一个习惯，写完内容之后就关闭

# 使用with：安全地关闭文件
with open("E:\\upload\\131.txt") as f:
    f.write("\nThis is about 'with...as...'")
with open("E:\\upload\\131.txt", "r") as f:
    print(f.read())