# -*-coding:utf-8 -*-
# *-*Author:DreamYee*-*
# Create:2019/12/04 18:12
# File:DemoF.py

import random
a=random.randint(100,999)
b=(a%10)*100+(a//10%10)*10+a//100
print(a,b)