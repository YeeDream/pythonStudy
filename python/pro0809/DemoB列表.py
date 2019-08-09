# -*-coding:utf-8 -*-
# *-*Author:DreamYee*-*
# Create:2019/08/09 8:23
# File:DemoB列表.py

#  函数：append  extend
a = [1,2,3]
b = ["python","java"]
c = a.extend(b)
d = b.extend(a)
print(a)
print(b)

# hasattr(变量名,'_iter_'):判断字符串是否可迭代
e = "python"
f = hasattr(e, '_iter_')
print(f)

e = [1,2]
f = hasattr(e,'_iter_')
print(f)

# 列表是可以修改的。这种修改，不是复制一个新的，而是在原地进行修改
# count():数一数某个元素在列表中出现了多少次
g = [1,2,1,1,3]
h = g.count(1)
print(h)
# index():检索元素在列表中的位置