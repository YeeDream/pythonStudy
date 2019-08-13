# -*-coding:utf-8 -*-
# *-*Author:DreamYee*-*
# Create:2019/08/13 9:03
# File:DemoA语句.py

import math
# 语句
# print
for i in [1,2,3,4,5]:
    print(i)

# import:引入模块
# import math
print(math.pow(3,2))
# pingfang()相当于重命名，意思跟pow()一样
from math import pow as pingfang
print(pingfang(3,2))

# 赋值语句
x, y, z = 1, "python", ["hello", "world"]
print(z)
a = 2
b = 9
# 将a与b的值调换
a,b = b, a
print(a,b)

x = 9
x += 1
print(x)

m = "py"
m += "th"
m += "on"
print(m)