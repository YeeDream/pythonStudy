# -*-coding:utf-8 -*-
# *-*Author:DreamYee*-*
# Create:2019/10/22 22:43
# File:DemoA.py

# 编写函数，判断一个数是否为素数，并编写主程序调用该函数

import math
def IsPrime(Num):
    if Num ==1:
        return False
    for n in range(2,int(math.sqrt(Num))+1):
        if Num%n==0:
            return False
        else:
            return True

n = input('输入你要判断的数：')
n = int(n)
if IsPrime(n)==True:
    print(n, '是素数')
else:
    print(n, '不是素数')
