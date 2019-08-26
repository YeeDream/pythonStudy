# -*-coding:utf-8 -*-
# *-*Author:DreamYee*-*
# Create:2019/08/26 15:25
# File:DemoA.py

# 参数收集
def func(x, *arg):
    print(x)
    result = x
    print(arg)
    for i in arg:
        result += i
        return result
print(func(1,2,3,4,5,6,7,8,9))

def foo(*args):
    print(args)
foo(1,2,3)
foo("qiwsir.github.io","python")
foo("qiwsir", 307, ["qiwsir", 2], {"name": "qiwsir", "lang": "python"})

# args收集到是一个空的tuple
def foo(x, *args):
    print("x:",x)
    print("tuple:",args)
foo(7)

# 用**kargs的形式收集值，会得到dict类型的数据，在传值的时候要说明键和值
def foo(**kargs):
    print(kargs)
foo(a = 1, b = 2, c = 3)

def foo(x, y, z, *args, **kargs):
    print(x)
    print(y)
    print(z)
    print(args)
    print(kargs)
foo('qiwsir', 2, "python")
foo(1,2,3,4,5)

def add(x, y):
    return x + y
print(add(2, 3))
# *是以元组形式传值，**是以字典形式传值
def book(author,name):
    print("%s is writing %s" % (author,name))
bars = {"name:""Starter learning Python", "author:""Kivi"}
book(*bars)

# 整理
'''
def foo(p1,p2,p3,...)
def foo(p1=value1,p2=value2,p3=value3,....)
def foo(*args)
def foo(**args)
'''