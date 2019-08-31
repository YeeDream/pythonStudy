# -*-coding:utf-8 -*-
# *-*Author:DreamYee*-*
# Create:2019/08/31 22:44
# File:DemoE.py

# heapq:堆（二叉树）
'''
特点：节点的值大于等于（或者小于等于）任何子节点的值。
     节点左子树和右子树是一个二叉堆。如果父节点的值总大于等于任何一个子节点的值，其为最大堆；
        若父节点值总小于等于子节点值，为最小堆。上面图示中的完全二叉树，就表示一个最小堆。
'''
# 堆的存储
import heapq
print(heapq.__all__)
# heappush(heap,x):将x压入堆heap（这是一个列表）
import heapq
heap = []
heapq.heappush(heap, 3)
heapq.heappush(heap, 9)
heapq.heappush(heap, 2)
heapq.heappush(heap, 4)
heapq.heappush(heap, 0)
heapq.heappush(heap, 8)
print(heap)

# heappop(heap):删除最小元素
print(heapq.heappop(heap))
print(heap)

# heapify():将列表转换为堆
h1 = [2,4,6,8,9,0,1,5,3]
print(heapq.heapify(h1))
print(h1)
heapq.heappop(h1)
heapq.heappop(h1)
print(h1)
heapq.heappush(h1,9)
print(h1)
# heapq.heappush(h1,"q")
print(h1)

# heapreplace():删除一个，同时加入一个
print(heap)
print(heapq.heapreplace(heap, 3.14))
print(heap)

# deque模块
from collections import deque
lst = [1,2,3,4]
qlst = deque(lst)
print(qlst.pop())
