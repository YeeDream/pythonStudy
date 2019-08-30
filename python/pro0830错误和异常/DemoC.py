# -*-coding:utf-8 -*-
# *-*Author:DreamYee*-*
# Create:2019/08/30 11:25
# File:DemoC.py

# assert
class Account(object):
    def __init__(self, number):self.number = number, self.balance = 0
    def deposit(self, amount):assert amount > 0
    def withdraw(self, amount): assert amount > 0
    if amount <= self.balance:
        self.balance -= amount
    else: print("balance is not enough.")
