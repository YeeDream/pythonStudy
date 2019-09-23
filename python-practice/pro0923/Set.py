# -*-coding:utf-8 -*-
# *-*Author:DreamYee*-*
# Create:2019/09/23 21:44
# File:Set.py

# 集合的创建与删除
a = {3, 5}
a.add(7)
print(a)
a_set = set(range(8, 14))
print(a_set)
b_set = set([0, 1, 2, 3, 0,1, 2, 3, 7, 8]) # 如果有重复元素，则在转换集合时保留一个
print(b_set)
x = set()  # 空集合

# pop():弹出并删除一个元素
# clear():清空集合删除所有元素
# remove():直接删除指定元素
a = {1,4,2,3}
print(a.pop())
print(a)
print(a.clear())

# 集合操作
a_set=set([8,9,10,11,12,13])
b_set=set([0,1,2,3,7,8])
print(a_set|b_set) # 并集
print(a_set.union(b_set))  # 并集
print(a_set & b_set)  # 交集
print(a_set.intersection(b_set))  # 交集
print(a_set.difference(b_set))  # 差集
print(a_set-b_set)  # 差集
print(a_set.symmetric_difference(b_set))  # 对称差
print(a_set ^ b_set)  # 对称差

x = {1,2,3}
y = {1,2,5}
z = {1,2,3,4}
print(x < y)  # 比较集合大小
print(x < z)
print(y < z)
print(x.issubset(y))   # 测试是否为子集
print(x.issubset(z))
