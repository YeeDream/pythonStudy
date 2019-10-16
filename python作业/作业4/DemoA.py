# -*-coding:utf-8 -*-
# *-*Author:DreamYee*-*
# Create:2019/10/16 21:20
# File:DemoA.py

# 1.通过Input（）函数任意输入三条边长，经过简单的计算后，判断三条边长能否构成三角形，并确定是类型的三角形，
# 如（等边，等腰，一般三角形）。
a = input("请输入长度：")
b = input("请输入长度：")
c = input("请输入长度：")
if a+b>c and a+c>b and b+c>a:
    if a==b==c:
        print("该三角形是等边三角形");
    elif a==b or a==c or b==c:
        print("该三角形是等腰三角形")
    else:
        print("该三角形是一般三角形！")
else:
    print("不满足构成三角形的条件")

