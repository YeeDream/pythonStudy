# -*-coding:utf-8 -*-
# *-*Author:DreamYee*-*
# Create:2019/12/04 18:14
# File:DemoG.py

x=eval(input('Please input x:'))
if x<0 or x>=20:
    print(x//10)
elif 0<=x<5:
    print(x)
elif 5<=x<10:
    print(3*x-5)
elif 10<=x<20:
    print(0.5*x-2)

for i in range(1,21,5):
    print(i,end=' ')

for i in range(10,1,-2):
    print(i,end=' ')

i =-1
while(i<0):
    i=i*1
    print(i)