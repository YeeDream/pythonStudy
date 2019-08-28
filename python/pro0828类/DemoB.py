# -*-coding:utf-8 -*-
# *-*Author:DreamYee*-*
# Create:2019/08/28 18:52
# File:DemoB.py

# 调用绑定方法
class Person(object):
    def foo(self):pass
pp = Person()

# 静态方法和类方法
__metaclass__ = type
class StaticMethod:
    @staticmethod
    def foo():
        print("This is static method foo().")
class ClassMethod:
    @classmethod
    def bar(cls):print("This is class bar().")
# @staticmethod 下面是静态方法
# @classmethod  下面是类方法
print(StaticMethod.foo())

# 文档字符串
def start_func(arg):
    '''This is a function'''
    pass
class Myclass:
    '''This is a class'''
def my_method(self, arg):
    '''This is my method.'''
    pass
