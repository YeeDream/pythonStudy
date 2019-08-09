# -*-coding:utf-8 -*-
# *-*Author:DreamYee*-*
# Create:2019/08/09 8:22
# File:DemoA列表.py

# [] 列表,list
a = []
print(type(a))
print(bool(a))
a =['a', 3, "dream"]
print(a)
# 索引和切片
print(a[2])
b = a.index(3)
print(b)
# 编号方式：从最右边开始，-1，向左依次是-2，-3....(字符串，列表都适用)
print(a[-1])
# 对于切片要注意：序列的切片，左边的数字小于右边的数字
c = "python"
d = c[-3:-1]
print(d)

# 反转 [::-1]    list(reversed(变量名))
e = [1,2,3,4,5]
f = e[::-1]
print(f)
g = list(reversed(e))
print(g)

print(list(reversed("abc")))

#  list操作
'''
len():长度
+：连接两个序列
*：重复元素
in:判断某一序列是否在一个序列
max(),min()
'''
h = ['python','java','c++']
print('java' in h)

# 追加元素  list.append()等同于a[len(a):] = [x]
i = ["good","python","I"]
m = i.append("like")
print(i)
n = i[3:] = ["like"]
print(i)
