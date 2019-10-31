# -*-coding:utf-8 -*-
# *-*Author:DreamYee*-*
# Create:2019/10/31 19:49
# File:Fib.py

# 1、编写一函数Fabonacci(n)，其中参数n代表第n次的迭代。
def Fabonacci(n):
    a,b=0,1
    while n>0:
        a,b=b,a+b
        n-=1
        yield a
n = int(input("输入一个数："))
for i in Fabonacci(n):
    print(i)