# -*-coding:utf-8 -*-
# *-*Author:DreamYee*-*
# Create:2019/08/13 9:15
# File:DemoB语句.py

# if
a = 8
if a == 8:
    print(a)

# if/else/else if
number = int(input())
if number == 10:
    print("您输入的数字是：",number)
else:
    print(3)

# 三元操作符
name = "dream" if "laoqi" else "github"
name = 'laoqi'
print(name)
# A=Y if X else Z:如果X为真，就执行：A=Y;X为假，就执行：A=Z
x = 2
y = 8
a = "python" if x>y else "dream"
print(a)
b = "python" if x<y else "dream"
print(b)