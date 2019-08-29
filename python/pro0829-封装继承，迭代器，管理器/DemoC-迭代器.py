# -*-coding:utf-8 -*-
# *-*Author:DreamYee*-*
# Create:2019/08/29 16:06
# File:DemoC-迭代器.py
class MyRange(object):
    def __init__(self, n):self.i = 0
    def __iter__(self):return self
    def next(self):
        if self.i :
            i =self.i
            self.i +=1
            return i
        else:
            StopIteration()
if __name__ =="__main__":
    x =MyRange(7)
print("x.next()==>", x.next())
print("x.next()==>",x.next())
print("------for loop--------")
for i in x:
    print(i)
