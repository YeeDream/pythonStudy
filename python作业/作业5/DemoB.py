# -*-coding:utf-8 -*-
# *-*Author:DreamYee*-*
# Create:2019/10/16 23:38
# File:DemoB.py

# 我国有13 亿人口，如果按人口年增长0.8%计算，多少年后将达到26 亿？
n = 13  # 人口
y = 0   # 年
while n < 26:
    y += 1
    n = n*(1+0.008)
print(y,"年后将达到26亿")