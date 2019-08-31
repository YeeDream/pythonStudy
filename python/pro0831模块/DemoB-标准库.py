# -*-coding:utf-8 -*-
# *-*Author:DreamYee*-*
# Create:2019/08/31 13:50
# File:DemoB-标准库.py

# 引用的方式 : import modulename
import pprint
a = {"lang":"python", "book":"www.itdiffer.com", "teacher":"dream", "gobal":"from beginer to master"}
pprint.pprint(a)

from pprint import pprint
print(a)

from pprint import *

import pprint as pr
pr.pprint(a)

from pprint import pprint as pt
pt(a)

import pprint
print(dir(pprint))

[m for m in dir(pprint) if not m.startwith(".")]

# 帮助，文档，源码
help()
dir()

