# -*-coding:utf-8 -*-
# *-*Author:DreamYee*-*
# Create:2019/08/29 15:24
# File:DemoA-多态继承.py

# 多态
# count()数一数某个元素在对象中出现的次数
print("This is a book.".count("s"))
print([1,2,3,4,5].count(3))

f = lambda x, y:x+y
print(f(2,3))

# repr():针对输入的任何对象返回一个字符串
print(repr([1,2,3]))

def length(x):
    print("The length of",repr(x),"is",len(x))
length("how are you")

# 封装和私有化
__metaclass__ = type
class ProtectMe:
    def __init__(self):self.me = "dream"
    @property
    def name(self):return self.__name
    def __python(self):print("I love python.")
    def code(self):print("Which language do you like?")
if __name__ == "__main__":
     p = ProtectMe()
     p.code()
print(p.me)
# print(p.__name)
