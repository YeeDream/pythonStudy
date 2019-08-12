# -*-coding:utf-8 -*-
# *-*Author:DreamYee*-*
# Create:2019/08/12 19:22
# File:DemoA集合.py

# 集合
# 创建set:{}其中的元素没有序列，元素不可重复
s1 = set("dream")
print(s1)
s2 = set([123, "google", "face", "book", "facebook", "book"])
print(s2)
# 通过{}直接创建
s3 ={"facebook", 123}
print(s3)
# 错误：s3 = {"facebook", [1, 2, 'a'], {"name": "python", "lang": "english"}, 123}

# list()与set()的转化
lst = list(s1)
print(lst)
lst[1] = "I"
print(lst)

# 集合的方法
# add  update
a_set = {'a', 'i'}
# add():增加一个元素
a_set.add("dream")
print(a_set)
# update():从另外一个set中合并过来元素
s1 = set(['a', 'b'])
s2 = set(['github', 'dream'])
# 把s2的元素并入s1中
s1.update(s2)
print(s1)

# pop():从set中任意选一个元素，删除并将这个值返回
b_set= set(['[1,2,3]', 'h', 'o', 'n', 'p', 't', 'dream', 'y'])
b_set.pop()
print(b_set)
# remove():删除指定的元素；如果不是set中的元素就会报错
a_set = set(['i', 'a', 'dream'])
a_set.remove('i')
print(a_set)
# discard():如果是set中的元素，就删除；如果不是，就什么也不做
a_set.discard('a')
print(a_set)
a_set.discard('b')
print(a_set)
# clear():删除set中的所有元素
a_set.clear()
print(a_set)
print(bool(a_set))




