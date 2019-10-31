# -*-coding:utf-8 -*-
# *-*Author:DreamYee*-*
# Create:2019/10/31 20:32
# File:twistPrime.py

# 3、利用上题中判断素数的函数，编写程序找出1~100 之间的所有孪生素数
# （若两个素数之差为2，则这两个素数就是一对孪生素数） 。
# 例如：3 和5、5 和7、11和13 等都是孪生素数。

def prime(n):
    if n<2:
        return False
    a=0
    for i in range(1,n+1):
        if n%i==0:
            a+=1
    if a>2:
        return False  # 不是素数
    else:
        return True   # 是素数

def main():
    for i in range(1,100):
        if prime(i) and prime(i+2):
            print(i,i+2)

main()