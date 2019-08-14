# -*-coding:utf-8 -*-
# *-*Author:DreamYee*-*
# Create:2019/08/14 18:32
# File:DemoA语句.py

# 求两个列表的和
a = [1,2,3,4,5]
b = [9,8,7,6,5]
c = []
for i in range(len(a)):
    c.append(a[i]+b[i])
print(c)

# zip()
a = "qiwir"
b = "github"
print(list(zip(a,b)))
c = [1,2,3]
d = [9,8,7,6]
print(list(zip(c,d)))

a = [1,2,3,4,5]
b = ["python", "www.baidu.com", "dream"]
length = len(a) if len(a)<len(b) else len(b)
print(length)
for i in range(length):
    c.append(str(a[i])+":"+b[i])
print(c)

# enumerate
seasons = ['spring', 'summer', 'fall', 'winter']
print(list(enumerate(seasons)))
print(list(enumerate(seasons,start=1)))

# 问题：将字符串中的某些字符替换为其它的字符串。
# 原始字符串"Do you love Canglaoshi? Canglaoshi is a good teacher."，请将"Canglaoshi"替换为"PHP".
raw = "Do you love China? China is a good country."
raw_list = raw.split(" ")
for i, string in enumerate(raw_list):
    if string == "China":
        raw_list[i] = "PHP"
print(raw_list)

for i, string in enumerate(raw_list):
    if "China" in string:
        raw_list[i] = "PHP"
print(raw_list)

# list解析
power2 = []
for i in range(1,10):
    power2.append(i*i)
print(power2)

squares = [x**2 for x in range(1,10)]
print(squares)
