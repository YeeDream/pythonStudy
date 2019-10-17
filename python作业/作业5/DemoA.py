# -*-coding:utf-8 -*-
# *-*Author:DreamYee*-*
# Create:2019/10/16 23:38
# File:DemoA.py

# 1.编写程序解决爱因斯坦台阶问题：有人走一台阶，若以每步走两级则最后剩下一级；
# 若每步走三级则剩两级；若每步走四级则剩三级；
# 若每步走五级则剩四级；若每步走六级则剩五级；
# 若每步走七级则刚好不剩。问台阶至少共有多少级？

import math
l=[]
for x in range(0,1000):
    if x%2==1 and x%3==2 and x%4==3 and x%5==4 and x%6==5 and x%7==0:
        l.append(x)
print("至少有",min(l),"个台阶。")