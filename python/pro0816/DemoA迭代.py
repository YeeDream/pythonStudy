# -*-coding:utf-8 -*-
# *-*Author:DreamYee*-*
# Create:2019/08/16 16:30
# File:DemoA迭代.py

'''
循环（loop），指的是在满足条件的情况下，重复执行同一段代码。比如，while语句。
迭代（iterate），指的是按照某种顺序逐个访问列表中的每一项。比如，for语句。
递归（recursion），指的是一个函数不断调用自身的行为。比如，以编程方式输出著名的斐波纳契数列。
遍历（traversal），指的是按照一定的规则访问树形结构中的每个节点，而且每个节点都只访问一次。
'''

# 逐个访问
lst = ['d', 'r','e', 'a', 'm']
for i in lst:
    print(i)
print("******************")

lst_iter = iter(lst)
# __next__():获得下一个元素
print(lst_iter.__next__())
'''
while True:
    print(lst_iter.__next__())
'''

# 文件迭代器
f = open("E:\\upload\\208.txt")
print(f.readline())
print(f.readline())
print(f.readline())

f = open("E:\\upload\\208.txt")
for line in f:
    print(line)

# 列表
print([line for line in open("E:\\upload\\208.txt")])

print(list(open("E:\\upload\\208.txt")))