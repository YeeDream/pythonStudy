# -*-coding:utf-8 -*-
# *-*Author:DreamYee*-*
# Create:2019/08/17 9:40
# File:DemoA函数.py

# 深入理解函数
# 建立简单函数
a = 2
y = 3*a + 2
print(y)

# 建立实用的函数
def name():
    print("dream")
name()

def add(x,y):
    print(x+y)
add(3,4)
# python中为对象编写接口，而不是数据类型

# 调用函数
def add(x,y):
    print("x=",x)
    print("y=",y)
    return x+y
add(x=10,y=3)

def times(x, y = 2):
    print("x=",x)
    print("y=",y)
    print(x*y)
times(3)

'''
1.不要忘了冒号:
2.从第一行开始
3.空白行在交互模式提示符下面很重要
4.缩进要一致
5.使用简洁的for循环
6.注意赋值语句的可变对象
7.不要期待在原处修改的函数会返回结果
8.调用函数时，函数名后面一定要跟随着括号
9.不要在导入和重载中使用扩展名或路径
'''