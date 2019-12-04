# -*-coding:utf-8 -*-
# *-*Author:DreamYee*-*
# Create:2019/12/04 19:57
# File:DemoI.py

x=30
def func():
    global x
    x=20
func()
print(x)

counter=0;num=0
def Test():
    global counter
    for i in range(4):counter+=1
    num=5
Test()
print(counter,num)