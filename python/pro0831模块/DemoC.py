# -*-coding:utf-8 -*-
# *-*Author:DreamYee*-*
# Create:2019/08/31 14:01
# File:DemoC.py

# sys
import sys
print(sys.__doc__)  # 显示了sys的基本文档
# sys.argv向python解释器传递参数   命令行参数
import sys
print("The file name:",sys.argv[0])
print("The number of argument",len(sys.argv))
print("The argument is:",str(sys.argv))
# sys.exit():退出当前的程序
'''
import sys
for i in range(10):
    if i == 5:
        sys.exit()
    else:
        print(i)
'''
# sys.path:查找模块所在的目录
# sys.sdin   sys.stdout  sys.stderr
# 都是类文件流对象，分别表示标准输入、标准输出、标准错误

for i in range(3):
    print(sys.stdout.write(str(i)+'\n'))

# copy
import copy
print(copy.__all__ ['Error', 'copy', 'deepcopy'])

import copy
class MyCopy(object):
    def __init__(self, value):self.value = value
    def __repr__(self):return self.value
foo = MyCopy(7)
a = ["foo", foo]
b = a[:]
c = list(a)
d = copy.copy(a)
e = copy.deepcopy(a)
a.append("abc")
foo.value = 17
print("original: %r\n slice: %r\n list(): %r\n copy(): %r\n deepcopy(): %r\n" % (a,b,c,d,e))
