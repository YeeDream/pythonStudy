# -*-coding:utf-8 -*-
# *-*Author:DreamYee*-*
# Create:2019/09/11 21:43
# File:DemoC-二叉树.py

import BinaryTree
root = BinaryTree.BinaryTree('root')
b = root.insertRightChild('B')
a = root.insertLeftChild('A')
c = a.insertLeftChild('C')
d = c.insertRightChild('D')
e = b.insertRightChild('E')
f = e.insertLeftChild('F')
print(root.inOrder())
print(root.postOrder())
print(b.inOrder())
