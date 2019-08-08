# Author:DreamYee
# Create:2019/08/08 9:55
# File:DemoC字符串.py

#  索引和切片
lang = "study python"
print(lang[0])
print(lang.index("p"))

# 从2索引开始，到9之前(包括2但不包括9)
a = lang[2:9]
print(a)
# 切片：通过索引得到字符的过程

# 在获取切片的时候，如果冒号前面或者后面的序号没写，就表示是到最后或第一个
b = lang[1:]
c = lang[:8]
print("b:["+b+"]")
print(c)
d = lang[:]
print(d)

# id()作用是查看该对象的内存地址
print(id(lang))
print(id(d))
e = lang  # 等同于d = lang[:]
print(id(e))

# 字符串基本操作
'''
len():求序列长度
·：连接2个序列
·：重复序列元素
in:判断元素是否在序列中
max():返回最大值
min():返回最小值
cmp(str1,str2):比较2个序列值是否相同
'''
# +:连接字符串
str1 = "abc"
str2 = "def"
print(str1+str2)

# in
print("a" in str1)

# 最值
x = max(str1)
print(x)
y = min(str1)
print(y)

# 比较 > >= < <= ==
print((str1 == str2))
# ord():将字符转换成ASCII码
# chr()：将ASCII码转换成字符
print(ord('a'))
print(chr(98))
# *:重复某一字符串
print(str1*3)
print("-"*20)

# len()
r = len(str1)
print(r)
print(type(r))