# -*-coding:utf-8 -*-
# *-*Author:DreamYee*-*
# Create:2019/08/14 19:01
# File:DemoB语句.py

# 做猜字游戏
import random
i = 0
'''
while i < 4:
     print("**************")
 #   num = input("请输入0-9任何一个数：")
xnum = random.randint(0,9)
'''

# break:要在这个地方中断循环，跳出循环体
# continue:从当前位置跳到循环体的最后一行的后面(不执行最后一行)
a = 8
while a:
    if a % 2 == 0:
        break
    else:
        print("%d is odd number %a")
a = 0
print("%d is odd number %a")

# while...else
count = 0
while count < 5:
    print(count, "is less than 5")
    count = count + 1
else:
    print(count," is not less than 5")

# for...else
from math import sqrt
for n in range(99, 1, -1):
    root = sqrt(n)
    if root == int(root):
        print(n)
        break
    else:
        print("Nothing")