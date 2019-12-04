# -*-coding:utf-8 -*-
# *-*Author:DreamYee*-*
# Create:2019/12/04 18:22
# File:DemoH.py

import math
n=0
for m in range(101,201,2):
    k=int(math.sqrt(m))
    for i in range(2,k+2):
        if m%i==0:break
    if i==k+1:
        if n%10==0:print()
        print('%d'%m,end=' ')
        n+=1

a=[1,2,3,None,(),[],]
print(len(a))

s1=[4,5,6]
s2=s1
s1[1]=0
print(s2)

s=['a','b']
s.append([1,2])
s.insert(1,7)
print(s)

from math import *
for i in range(100,1000):
    n1=i//100;n2=(i%100)//10;n3=i%10;
    if(pow(n1,3)+pow(n2,3)+pow(n3,3)==i):
        print(i,end=' ')

sum=1;
for i in range(1,101):
    if i%7==0 and i%3!=0:
        print(i)
        sum*=i;
print(sum)

fruits=['apple','banana','pear']
print('Apple' in fruits)

# print('%d%d%'%(3/2,3%2))


str=input("input:")
count=0
flag=0
for c in str:
    if c==" ":
        flag=0
    else:
        if flag==0:
            flag=1
            count=count+1
print(count)