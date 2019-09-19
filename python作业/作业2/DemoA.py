# -*-coding:utf-8 -*-
# *-*Author:DreamYee*-*
# Create:2019/09/17 10:54
# File:DemoA.py

# 1.
mytup=[1,2,3,4,5,6,7,8,9,10]
print(mytup[:3])
print(mytup[-1])
print(max(mytup))
print(len(mytup))

# 2.产生一个1-26 的数字列表A
print(list(range(1,27,1)))

# 3.产生一个“ A”- “Z”的字母列表
b = []
for i in range(65, 91):
    b.append(chr(i))
print(b)

# 4.请生成一个字典mydict ，使得数字与字符形成对应，
# 如1）： ”A”,2: ”B”⋯⋯ 26: ” Z”
a = list(range(1,27,1))
keys = a
values = b
dictionary = dict(zip(keys,values))
print(dictionary)

# 5.已知ListA=[1,2,3,4,5], ListB= [ ‘one ’, ’two ’, ’three ’,’four ’, ’five ’], 请把两个列表合并成字典。
ListA=[1,2,3,4,5]
ListB= ['one ', 'two ', 'three ','four', 'five ']
dictionary=dict(zip(ListA,ListB))
print(dictionary)

# 6.使用字典来创建程序，提示用户输入电话号码，并用英文单词形式显示数字。例如：输入138 显示为“one three eight ”
a =[i for i in range(0,10)]
b = ['zero','one','two','three','four','five','six','seven','eight','nine']
mydict = dict(zip(a,b))
print("请输入电话号码：")
input()
for i in range(0,10):
    print(mydict(i))

# 7.莫尔斯电码采用了短脉冲和长脉冲（分别为点和点划线） 来编码字母和数字。例如，字母“A”是点划线，“B”是点划线点点。

