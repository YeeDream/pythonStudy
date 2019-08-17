# -*-coding:utf-8 -*-
# *-*Author:DreamYee*-*
# Create:2019/08/17 10:52
# File:DemoB函数.py

# 返回值
def fibs(n):
    result = [0,1]
    for i in range(n-2):
        result.append(result[-2]+result[-1])
        print(result)
lst = fibs(10)
print(lst)

def my_fun():
    return 1,2,3
a = my_fun()
print(a)

def my_fun():
    print("I am doing something.")
    return
    print("I finished")
a = my_fun()
print(a)

# 函数中的文档
# 全局变量和局部变量
x = 2
def funcx():
    x = 9
    print("This x is in the funcx", x)
    funcx()
    print("-----------------------")
    print("this x is out of funcx:",x)

x = 7
scope = vars()
print(scope['x'])
scope['x']+=1
print(x)
print(scope['x'])