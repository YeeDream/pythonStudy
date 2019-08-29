# -*-coding:utf-8 -*-
# *-*Author:DreamYee*-*
# Create:2019/08/29 15:41
# File:DemoB-特殊方法.py

# __dict__:对象的属性
class A(object):
    pass
a = A()
print(dir(a))

class Spring(object):
    season = "the spring of class"
print(Spring.__dict__)
print(Spring.__dict__['season'])

# __slots__:限制属性的定义   优化内存使用
class Spring(object):
    __slots__ = ("tree", "flower")
print(dir(Spring))
t = Spring()
print(t.__slots__)

# __getattr__    __setattr__
'''
__setattr__(self, name, value):如果要给name赋值，就调用这个方法
__getattr__(self, name):如果name被访问，同时它不存在的时候，就调用这个方法
__getattribute__(self, name):当name被访问时自动被调用，无论name是否存在，都要被调用
__delattr__(self, name):如果要删除name，就调用这个方法
'''
class A(object):
    def __getattr__(self, name):print("You use getattr")
    def __setattr__(self, name, value):print("You use setattr")
# a = A()
a.x = 7
print(a.x)

class B(object):
    def __getattribute__(self, name):print("you are using getattribute")
b = B()
b. y = 8
print(b.y)

# 获得属性顺序
class A(object):
    author = "dream"
    def __getattr__(self, name):
        if name != "author":return "from starter to master"
if __name__ == "__main__":
    a = A()
print(a.author)
print(a.lang)

