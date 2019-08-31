# -*-coding:utf-8 -*-
# *-*Author:DreamYee*-*
# Create:2019/08/31 13:09
# File:DemoA-编写模块.py

import math
print(math.pow(3, 2))

lang = "python"

def lang():
    return "python"
if __name__ == "__main__":
    print(lang())

import sys
sys.path.append("~/Documents/VBS/StarterLearningPython/2code/pm.py")
