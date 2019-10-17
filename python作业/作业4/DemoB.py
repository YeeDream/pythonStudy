# -*-coding:utf-8 -*-
# *-*Author:DreamYee*-*
# Create:2019/10/16 21:42
# File:DemoB.py

# 2.密码登录程序。
# 要求：建立一个登录窗口,要求输入帐号和密码。设定用户名为”zhangshan”，密码为“Python123”;
# 若用户名正确，密码正确，则显示 “Zhangshan先生，欢迎你 !”;
# 如果用户名错误，则显示“用户名错误，请重新输入! ”; 若密码不正确,显示“对不起,密码错误,无法登录! ”。

x = input("用户：")
y = input("密码：")
if x=="Zhangshan" and y !="Python123":
    print("对不起,密码错误,无法登录!")
if x=="Zhangshan"and y== "Python123":
    print("Zhangshan先生，欢迎你 !")
if x!="Zhangshan" and y!="Python123":
    print("用户名不存在，请查证！")
while x!="Zhangshan" and y=="Python123":
    x = input("请重新输入用户名：")
    if x=="Zhangshan":
        print("Zhangshan先生，欢迎你 !")

