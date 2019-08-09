# -*-coding:utf-8 -*-
# *-*Author:DreamYee*-*
# Create:2019/08/09 8:23
# File:DemoD.py

#  回顾list与str
'''
相同点：都是属于序列类型的数据
不同点：list是可以改变的，str不可变
       多维list:在str中，里面的每个元素只能是字符；在list中，元素可以是任何类型的数据
'''

# list与str的转化
# str.split():将str转化为list
line = "Hello.I am Dream.Welcome you."
a= line.split(".")
print(a)
print(line.split(".",1))
s = "I am,writting\npython\tbook on line"
print(s)
print(s.split())

# "[sep]".join(list)    join可以说是split的逆运算
name = ['Albert','Ainstain']
b = ".".join(name)
print(b)
print(" ".join(s.split()))


