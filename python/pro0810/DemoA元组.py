# -*-coding:utf-8 -*-
# *-*Author:DreamYee*-*
# Create:2019/08/10 10:38
# File:DemoA元组.py

# tuple(元组) 定义
a = 123, 'abc', ["come", "here"]
print(a)
# 元组是用圆括号起来的，其中的元素之间用逗号隔开
# 序列类型的数据，元素不能更改，可以是任何类型的数据

# 索引和切片
b = (1,'23',[123,'abc'],('python','learn'))
print(b[2])

print(b[1:])
print(b[2][0])

c = (3)
d = (3,)
print(type(c))
print(type(d))

# list()与tuple()转化
e = (1,'23',[123,'abc'],('python','learn'))
f = list(e)   # tuple--->list
print(f)
e = [1,'23',[123,'abc'],('python','learn')]
g = tuple(e)   # list--->tuple
print(g)

'''
tuple的特点：
1.tuple比list操作速度快
2.如果对不需要修改的数据进行 “写保护”，可以使代码更安全。
使用 tuple 而不是 list 如同拥有一个隐含的 assert 语句，说明这一数据是常量。
如果必须要改变这些值，则需要执行 tuple 到 list 的转换 (需要使用一个特殊的函数)。
3.Tuples 可以在 dictionary（字典，后面要讲述） 中被用做 key，但是 list 不行。
Dictionary key 必须是不可变的。
Tuple 本身是不可改变的，但是如果您有一个 list 的 tuple，那就认为是可变的了，用做 dictionary key 就是不安全的。
只有字符串、整数或其它对 dictionary 安全的 tuple 才可以用作 dictionary key。
4.Tuples 可以用在字符串格式化中。
'''