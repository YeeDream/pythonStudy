# -*-coding:utf-8 -*-
# *-*Author:DreamYee*-*
# Create:2019/10/31 20:39
# File:豆堆.py
# 思考题.豆堆
# 堆里有16颗豆子，有两个玩家（假设一个玩家是电脑） 。
# 每个玩家都可以从堆中的16颗豆子中取出1颗，2颗或者3颗豆子。每个玩家在每回合中必须从堆中取出一定数目的豆子。
# 玩家轮流取出豆子，取到最后一颗豆子的玩家是输家。
# 思路：写一个人取豆子的函数帮电脑设计一个算法，实现取豆子的函数在主程序中进行输流调用，谁最后拿到1粒豆子谁就输。
import random
def Peoplepick(n):  # 人取豆子
    while True:
        num = int(input("请取出一定数量的豆子，1颗，2颗或者3颗："))
        if num<1 or num>3:
            print("拿错了，重新拿：")
            continue
        return n-num

def Computerpick(n):# 电脑取豆子
    if n==4:
        return 3
    if n==3:
        return 2
    if n==2:
        return 1
    else:
        i = random.randint(1,3)
        return i

def main():
    total=16  # 总的豆子数
    while True:
        peopickRest = Peoplepick(total)  # 人取豆子后剩余的豆子
        compick = Computerpick(peopickRest)
        total = peopickRest - compick   #  人跟电脑取后剩余的豆子
        if peopickRest == 1:
            print("People win!")
            break
        print("电脑拿走的是：","compick=%d"%compick,"剩余的豆子：","rest=%d"%total)
        if total == 1:
            print("Computer win!")
            break

main()