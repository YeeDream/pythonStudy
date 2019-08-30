# -*-coding:utf-8 -*-
# *-*Author:DreamYee*-*
# Create:2019/08/30 11:05
# File:DemoB.py

while 1:
    print("this is a division program.")
    c = input("input 'c' continue ,otherwise logout:")
    if c == 'c':
        a = input("first number:")
        b = input("second number:")
        try: print(float(a)/float(b))
        except ZeroDivisionError: print("The second number can't be zero!")
        except ValueError: print("please input number.")
        else: break

try:
    print(1/0)
except:
    print("I am except")
else:
    print("I am else")

x = 10
try:
    x = 1/0
except Exception,e:print(e)
finally:print("del e")
