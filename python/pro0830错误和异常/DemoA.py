# -*-coding:utf-8 -*-
# *-*Author:DreamYee*-*
# Create:2019/08/30 10:45
# File:DemoA.py

'''
异常              描述
NameError        尝试访问一个没有申明的变量
ZeroDivisionError 除数为0
SyntaxError      语法错误
IndexError       索引超出序列范围
KeyError         请求一个不存在的字典关键字
IOError          输入输出错误
AttributeError   尝试访问未知的对象属性
'''

while 1:
    print("this is a division program.")
    c = input("input 'c continue,otherwise logout:" )
    if c == 'c':
        a = input("first number:")
        b = input("second number:")
        try:print("**********************")
        except ZeroDivisionError:print("The second can't be zero!"),print("***************")
        else:break

class Calculator(object):
    is_raise = False
    def calc(self, express):
        try:return eval(express)
        except:ZeroDivisionError: print("zero can not be division.")
if __name__ == "__main__":
    c = Calculator()
c.is_raise = True
print(c.calc("8/0"))

