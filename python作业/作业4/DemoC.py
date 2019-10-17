# -*-coding:utf-8 -*-
# *-*Author:DreamYee*-*
# Create:2019/10/16 21:42
# File:DemoC.py

# 3.设有三个变量a,b,c,分别对三个变量赋值，并对三个变量进行排序。
# 如a=5,b=7,c=6,则排序结果为b>c>a。

a = input("请输入一个数a=：")
b = input("请输入一个数b=：")
c = input("请输入一个数c=：")
if a>b>c:
    print("a>b>c")
elif a>c>b:
    print("a>c>b")
elif b>a>c:
    print("b>a>c")
elif b>c>a:
    print("b>c>a")
elif c>a>b:
    print("c>a>b")
elif c>b>a:
    print("c>b>a")

