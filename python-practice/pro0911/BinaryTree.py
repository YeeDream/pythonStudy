# -*-coding:utf-8 -*-
# *-*Author:DreamYee*-*
# Create:2019/09/11 21:44
# File:BinaryTree.py

# 自定义二叉树结构
class BinaryTree:
    def __init__(self,value):
        self._left=None
        self._right=None
        self._data=value

    def insertLeftChild(self,value):    # 创建左子树
        if self._left:
            print('left child tree already exists.')
        else:
            self._left=BinaryTree(value)
            return self._left

    def insertRightChild(self,value):  # 创建右子树
        if self._right:
            print('right child tree already exists.')
        else:
            self._right=BinaryTree(value)
            return self._right

    def show(self):
        print(self._data)

    def preOrder(self):   #前序遍历
        print(self._data)  # 输出根节点的值
        if self._left:
            self._left.preOrder()  # 遍历左子树
        if self._right:
            self._right.preOrder()  # 遍历右子树

    def postOrder(self):     #后序遍历
        if self._left:
            self._left.postOrder()
        if self._right:
            self._right.postOrder()
        print(self._data)

    def inOrder(self):  #  中序遍历
        if self._left:
            self._left.inOrder()
        print(self._data)
        if self._right:
            self._right.inOrder()

if __name__=='__main__':
    print('Please use me asa module.')
