# -*-coding:utf-8 -*-
# *-*Author:DreamYee*-*
# Create:2019/08/09 8:23
# File:DemoC列表.py

#  列表方法
# insert():在某个位置添加元素
a = ['python','java']
b = a.insert(1,'c++')
print(a)
len = len(a)
print(len)
c = a.insert(len,'github')
print(a)
d = [1,2,3]
d.insert(9,777)
print(d)

#删除元素
# pop([i])   remove(x)
e = a.pop()
f = d.remove(3)
print(a)
print(d)

# reverse():列表中的元素反过来
g = [2,4,5]
g.reverse()
print(g)

# sort():对列表进行排序（从小到大）
h = [8,5,9,1]
h.sort()
print(h)
# 从大到小
h.sort(reverse=True)
print(h)

# 以字符串的长度为关键字进行排序
m = ["python", "c", "pascal", "basic"]
m.sort(key=len)
print(m)