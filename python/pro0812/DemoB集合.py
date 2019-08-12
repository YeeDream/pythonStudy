# -*-coding:utf-8 -*-
# *-*Author:DreamYee*-*
# Create:2019/08/12 20:08
# File:DemoB集合.py

# 元素与集合的关系 ：要么属于某个集合，要么不属于
aset = set(['h', 'o', 'n', 'p', 't', 'y'])
print("a" in aset)
print("h" in aset)

# 集合与集合的关系
a = set(['q', 'i', 's', 'r', 'w'])
b = set(['a', 'q', 'i', 'l', 'o'])
print(a == b)
print(a != b)
# 判断集合A是否是集合B的元素：A<B或者A.issubset(B)
# 判断c是a的子集
a = set(['q', 'i', 's', 'r', 'w'])
c = set(['q', 'i'])
print(c < a)
# 判断a是c的超集
print(a.issuperset(c))

# 两个集合的并集：A|B或者A.union(B),   这个结果是新生成的一个对象，不是将A扩充
a = set(['q', 'i', 's', 'r', 'w'])
b = set(['a', 'q', 'i', 'l', 'o'])
print(a|b)

# 两个集合的交集 A&B   A.intersection(B)
print(a&b)

# A相对B的差集（补集）：A and B
print(a and b) # a相对b不同部分的元素

# -A、B的对称差集:a - b或者a.difference(b)
print(a - b)
a = set(['q', 'i', 's', 'r', 'w'])
b = set(['a', 'q', 'i', 'l', 'o'])
a.symmetric_difference(b)

