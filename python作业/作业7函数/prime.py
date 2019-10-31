# -*-coding:utf-8 -*-
# *-*Author:DreamYee*-*
# Create:2019/10/31 20:19
# File:prime.py

# 2、编写一函数Prime(n)，对于已知正整数n，判断该数是否为素数，
# 如果是素数，返回True,否则返回False。
def Prime(n):
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
    n = int(input("请输入一个数："))
    print(Prime(n))

main()