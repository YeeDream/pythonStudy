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
numWord = ["zero","one","two","three","four","five","six","seven","eight","nine"]
phoneNum = str(input("输入电话号码："))
for i in range(len(phoneNum)):
    getNum = ord(phoneNum[i])-ord('0')
    print(numWord[getNum], end=" ")

# 7.莫尔斯电码采用了短脉冲和长脉冲（分别为点和点划线） 来编码字母和数字。例如，字母“A”是点划线，“B”是点划线点点。
# 1）创建字典，将字符映射到莫尔斯电码。
# 2）输入一段英文，翻译成莫尔斯电文。
import string
def Mostran(wholetext):
    f = open("E:\\大三上\\python\\Mos.txt","r")
    Mostext = ""
    for line in f:
        Mostext += line
    f.close()
    Lwhole = Mostext.split()

    L1 = Lwhole[::2]    # 用这种间隔分片出来就是列表
    L2 = Lwhole[1::2]
    MosDict = dict(zip(L1, L2))

    for char in wholetext:
        print(MosDict[char])

def main():
    temp = input("\nEnter a passage:")
    temp = temp.upper()
    wholetext=""
    for char in temp:
        if char not in string.whitespace+string.punctuation:
            wholetext += char
        translation = Mostran(wholetext)
main()