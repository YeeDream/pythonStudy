# -*-coding:utf-8 -*-
# *-*Author:DreamYee*-*
# Create:2019/10/23 21:02
# File:DemoB.py

def MaxNum(num):
    sum = 0
    max = int(num[0])
    num = num.split(",")
    for i in range(len(num)):
        sum = sum + int(num[i])
        if(int(num[i]) > max):
            max = int(num[i])
    return sum,max

if __name__ == '__main__':
    num = input("请输入一些数：")
    sum,max=MaxNum(num)
    print("最大的数为：",max)
    print("整数之和为：",sum)
