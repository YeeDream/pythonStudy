# -*-coding:utf-8 -*-
# *-*Author:DreamYee*-*
# Create:2019/10/08 14:38
# File:DemoA.py

# 1.有一段英文，其中有单词连续重复了2次，编写程序检查重复的单词并只保留一个。
# 例如，文本内容为“This is is a desk.”，程序输出为“This is a desk.”
import re
x = 'This is is a desk.'
pattern = re.compile(r'\b(\w+)(\s+\1){1,}\b')
matchResult = pattern.search(x)
x = pattern.sub(matchResult.group(1), x)
print(x)

'''
# 2.编写程序，用户输入一段英文，然后输出这段英文中所有长度为3个字母的单词。
import re
x = input('Please input a string:')
pattern = re.compile(r'\b[a-zA-Z]{3}\b')
print(pattern.findall(x))
'''

