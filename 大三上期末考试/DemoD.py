# -*-coding:utf-8 -*-
# *-*Author:DreamYee*-*
# Create:2019/12/04 17:07
# File:DemoD.py

class Hello():
    def __init__(self,name):
        self.name=name
    def showInfo(self):
        print(self.name)

h=Hello('张三')
h.showInfo()
