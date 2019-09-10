# -*-coding:utf-8 -*-
# *-*Author:DreamYee*-*
# Create:2019/09/10 15:25
# File:DemoC.py

# 队列：先进先出，后进后出
import queue
q = queue.Queue()
q.put(0)
q.put(1)
q.put(2)
print(q.queue)
print(q.get())
print(q.queue)
print(q.get())
print(q.queue)

class myQueue:
    # 构造函数，默认队列大小为10
    def __init__(self,size=10):
        self._content=[]
        self._size=size
        self._current=0
    def setSize(self,size):
        if size<self._current:
            # 如果缩小队列，应删除后面的元素
            for i in range(size,self._current)[::-1]:
                del self._content[i]
            self._current=size
        self._size=size
    def put(self,v):
        if self._current<self._size:
            self._content.append(v)
            self._current=self._current+1
        else:
            print('The queue is full')

    def get(self):
        if self._content:
            self._current=self._current-1
            return self._content.pop(0)
        else:
            print('The queue is empty')

    def isEmpty(self):
        if not self._content:
            return True
        else:
            return False

    def isFull(self):
        if self._current==self._size:
            return True
        else:
            return False

if __name__=='__main__':
    print('Please use me as a module.')

import myQueue
q = myQueue.myQueue()