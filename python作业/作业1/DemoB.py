# -*-coding:utf-8 -*-
# *-*Author:DreamYee*-*
# Create:2019/09/05 17:23
# File:DemoB.py

import math
r = input("请输入球体半径：")
r = float(r)
s = 4*math.pi*pow(r, 2)
print("球体的表面积为：",s)
v = (4/3)*math.pi*pow(r, 3)
print("球体的体积为：",v)
