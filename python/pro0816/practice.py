# -*-coding:utf-8 -*-
# *-*Author:DreamYee*-*
# Create:2019/08/16 16:51
# File:practice.py

# 1.有一个列表，其中包括10个元素，例如这个列表是[1,2,3,4,5,6,7,8,9,0],要求将列表中的每个元素一次向前移动一个位置，
# 第一个元素到列表的最后，然后输出这个列表。最终样式是[2,3,4,5,6,7,8,9,0,1]
raw = [1,2,3,4,5,6,7,8,9,0]
# pop():删除元素       append():追加元素
b = raw.pop(0)
raw.append(b)
print(raw)

'''
2.按照下面的要求实现对列表的操作：
产生一个列表，其中有40个元素，每个元素是0到100的一个随机整数
如果这个列表中的数据代表着某个班级40人的分数，请计算成绩低于平均分的学生人数，并输出
对上面的列表元素从大到小排序
'''
'''
import random
score = random.randint(0,100)
for i in random(40):
    print(score)
num = len(score)
'''

# 3.如果将一句话作为一个字符串，那么这个字符串中必然会有空格（这里仅讨论英文），
# 比如"How are you."，但有的时候，会在两个单词之间多大一个空格。
# 现在的任务是，如果一个字符串中有连续的两个空格，请把它删除。
string = "I love code"
print(string)
str_list = string.split(" ")
print(string)
words = [s for s in str_list if s!=""]
print(words)

# 4.斐波那切数列
a, b = 0, 1
for i in range(4):
    a, b = b, a+b
    print(a)