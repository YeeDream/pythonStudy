# -*-coding:utf-8 -*-
# *-*Author:DreamYee*-*
# Create:2019/09/11 21:06
# File:DemoA-栈.py

# 栈：先进后出或后进先出
# 列表对象的append()方法是在列表尾部追加元素，相当于入栈操作
# pop()方法默认是弹出并返回列表的最后一个元素，相当于出栈操作
myStack = []
myStack.append(3)
print(myStack.pop())
myStack.append(5)
print(myStack.pop())
myStack.append(7)
print(myStack.pop())
print(myStack)
# print(myStack.pop())    #  IndexError: pop from empty list

import Stack
s=Stack.Stack()
print(s.showRemainderSpace())
print(s)
print(s.isEmpty())
print(s.isFull())
s.push(5)
s.push(8)
s.push('a')
print(s.pop())
s.push('b')
s.push('c')
print(s.show())
