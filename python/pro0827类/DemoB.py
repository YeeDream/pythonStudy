# -*-coding:utf-8 -*-
# *-*Author:DreamYee*-*
# Create:2019/08/27 8:09
# File:DemoB.py
class AA:
    pass
aa = AA();
print(type(AA))
print(type(aa))
a = 7
print(a.__class__)
print(type(a))

class BB(object):
    pass
bb = BB()
print(bb.__class__)
print(aa)
print(bb)

'''
1.
class BB(object):
    pass
    
2.
在类的前面写上：__metaclass__ == type ，在定义类的时候就不再需要在名字后面写(object)
'''

# 创建类
# 定义类
class Person:
    pass
# 初始化
# def __init__

girl = Person("dream")
print(girl.name)

# 函数（方法）
def getName(self):
    return self.name
girl = Person("dream")
name = girl.getName()

def color(self, color):
    print("%s is %s" % (self.name, color))
girl.color("write")

'''
 类和实例
 类提供默认行为，是实例的工厂
 类是由一些语句组成，但是实例，通过调用类生成，每次调用一个类，就会得到这个类的新的实例
'''

# self的作用：接收实例化过程中传入的所有数据