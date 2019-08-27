# -*-coding:utf-8 -*-
# *-*Author:DreamYee*-*
# Create:2019/08/27 14:00
# File:DemoC.py

# 类属性和实例属性
class  A(object):
    x = 7
print(A.x)

foo = A()
print(foo.x)
foo.x += 1
print(foo.x)

class B(object):
    y = [1,2,3]
print(B.y)
bar = B()
print(bar.y)
bar.y.append(4)
print(bar.y)

# 数据流转
__metaclass__ = type
class Person:
    def __init__(self, name):self.name = name
    def getName(self):return self.name
    def breast(self, n):self.breast = n
    def color(self, color): print("%s is %s" % (self.name, color))
    def how(self): print("%s breast is %s" % (self.name, self.breast))
girl = Person('canglaoshi')
girl.breast(90)
girl.color("white")
print(girl.how())

# 命名空间
'''
内置命名空间
全局命名空间
本地命名空间
'''
def foo(num,str):
    name = "dream"
    print(locals())
print(foo(221,"dream.github.io"))

# 作用域
def outer_foo():
    a = 20
    def inner_foo():
        c = 30
        a = 10
print(outer_foo())