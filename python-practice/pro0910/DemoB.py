# -*-coding:utf-8 -*-
# *-*Author:DreamYee*-*
# Create:2019/09/10 9:34
# File:DemoB.py

# 堆:堆是一个二叉树，其中每个父节点的值都小于或等于其所有子节点的值
import heapq
import random
data = list(range(10))   # 随机打乱列表中元素的顺序
random.shuffle(data)
print(data)
heap = []
for n in data:       # 建堆
    heapq.heappush(heap,n)
print(heap)
heapq.heappush(heap,0.5) # 新数据入堆
print(heap)
print(heapq.heappop(heap))    # 弹出最小的元素，堆会自动重建
print(heapq.heappop(heap))
print(heapq.heappop(heap))

myheap = [1,2,3,5,7,8,9,4,10,333]
heapq.heapify(myheap)  # 将列表转化为堆
print(myheap)
heapq.heapreplace(myheap,6)   #  替换堆中的元素值，自动重新构建堆
print(myheap)
print(heapq.nlargest(3,myheap))   #  返回前3个最大的元素
print(heapq.nsmallest(3,myheap))   #  返回前3个最小的元素
