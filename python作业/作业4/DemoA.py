# -*-coding:utf-8 -*-
# *-*Author:DreamYee*-*
# Create:2019/10/16 21:20
# File:DemoA.py

# 1.通过Input（）函数任意输入三条边长，经过简单的计算后，判断三条边长能否构成三角形，并确定是类型的三角形，
# 如（等边，等腰，一般三角形）。
a = input("请输入长度：")
b = input("请输入长度：")
c = input("请输入长度：")
if a+b>c and a+c>b and b+c>a:
    if a==b==c:
        print("该三角形是等边三角形");
    elif a==b or a==c or b==c:
        print("该三角形是等腰三角形")
    else:
        print("该三角形是一般三角形！")
else:
    print("不满足构成三角形的条件")

# 2.密码登录程序。
# 要求：建立一个登录窗口,要求输入帐号和密码。设定用户名为”zhangshan”，密码为“Python123”;
# 若用户名正确，密码正确，则显示 “Zhangshan先生，欢迎你 !”;
# 如果用户名错误，则显示“用户名错误，请重新输入! ”; 若密码不正确,显示“对不起,密码错误,无法登录! ”。
