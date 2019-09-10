# -*-coding:utf-8 -*-
# *-*Author:DreamYee*-*
# Create:2019/09/10 9:03
# File:DemoA.py

# 内置方法sorted()
persons = [{'name':'Dong','age':37},{'name':'Zhang','age':40},{'name':'Li','age':50},{'name':'Dong','age':43}]
print(persons)
# 使用key来指定排序依据，先按姓名升序排序，姓名相同的按年龄降序排序
print(sorted(persons,key=lambda x:(x['name'],-x['age'])))

from timeit import Timer
# 在python2.7.11中比较sorted()方法的key参数与cmp参数对排序速度的影响
print(Timer(stmt='sorted(xs,key=lambda x:x[1])',setup='xs=range(100);xs=zip(xs,xs);').timeit(100000))
# print(Timer(stmt='sorted(xs,key=lambda a, b:cmp(a[1],b[1]))', setup='xs=range(100);xs=zip(xs,xs);').timeit(100000))

phonebook ={'Linda':'7750','Bob':'9375','Carol':'5834'}
from operator import itemgetter
print(sorted(phonebook.items(),key=itemgetter(1)))   # 按字典中元素值排序
print(sorted(phonebook.items(),key=itemgetter(0)))   # 按字典中元素的键排序

gameresult = [['Bob',95.0,'A'],['Alan',86.0,'C'],['Mandy',83.5,'A'],['Rob',89.3,'E']]
print(sorted(gameresult,key=itemgetter(0,1)))  # 按姓名升序，姓名相同的按分数升序排序
print(sorted(gameresult,key=itemgetter(1,0)))  # 按分数升序，分数相同的按姓名升序排序
print(sorted(gameresult,key=itemgetter(2,0)))  # 按等级升序，等级相同的按姓名升序排序

# 如何根据另外一个列表的值来对当前列表元素排序
list1= ["what","I'm","sorting","by"]
list2=["something","else","to","sort"]
pairs= zip(list1,list2)
pairs=sorted(pairs)
print(pairs)
result = [x[1] for x in pairs]
print(result)
