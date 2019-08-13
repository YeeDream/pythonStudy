# -*-coding:utf-8 -*-
# *-*Author:DreamYee*-*
# Create:2019/08/13 9:28
# File:DemoC语句.py

# for语句：for 循环规则:操作语句
hello = "world"
for i in hello:
    print(i)
for i in range(len(hello)):
    print(hello[i])

# range(start,stop[,step])
'''
这个函数可以创建一个数字元素组成的列表。
这个函数最常用于for循环
函数的参数必须是整数，默认从0开始。返回值是类似[start, start + step, start + 2*step, ...]的列表。
step默认值是1。如果不写，就是按照此值。
如果step是正数，返回list的最最后的值不包含stop值，即start+istep这个值小于stop；如果step是负数，start+istep的值大于stop。
step不能等于零，如果等于零，就报错。
'''

'''
start：开始数值，默认为0,也就是如果不写这项，就是认为start=0
stop：结束的数值，必须要写的。
step：变化的步长，默认是1,也就是不写，就是认为步长为1。坚决不能为0
'''
print(range(-9))

name_str = "qiwsir"
for i in name_str:
    print(i)

name_list = list(name_str)
print(name_list)

a_dict = {"name":"qiwsir", "lang":"python", "email":"qiwsir@gmail.com", "website":"www.itdiffer.com"}
for k in a_dict.keys():
    print(k,a_dict[k])