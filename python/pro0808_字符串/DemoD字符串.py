# Author:DreamYee
# Create:2019/08/08 12:49
# File:DemoD字符串.py

# 字符串格式化输出
# 格式化字符串，是C、C++等程序设计语言printf类函数中用于指定输出参数的格式与相对位置的字符串参数。
# 占位符：%s
print("I like %s" % "python")
print("My name is %s" % "DreamYee")
'''
占位符     说明
%s      字符串（采用str()的显示）
%r      字符串（采用repr()的显示）
%c      单个字符
%b      二进制整数
%d      十进制整数
%i      十进制整数
%o      八进制整数
%x      十六进制整数
%:e     指数（基底写为e）
%E      指数(基底写为E)
%f      浮点数
%F      浮点数
%g      指数(e)或浮点数(根据显示长度)
%G      指数(E)或浮点数(根据显示长度)
'''
a = "%d years" % 8
print(a)
print("Today's temperature is %.2f" % 12.325)
# string.format()
# {索引值}
b = "Suzhou is more than {year} years. {name} lives in here.".format(year=2500, name="Dream")
print(b)

# 字典格式化
lang = "Jackson Yee"
m = "Dream like %(program)s"%{"program":lang}
print(m)

# 常用的字符串方法
# split():将字符串根据某个字符进行分割
c = "I LOVE PYTHON"
d = c.split(" ")
print(d)

# 去掉字符串两头的空格
'''
S.strip() 去掉字符串的左右空格
S.lstrip() 去掉字符串的左边空格
S.rstrip() 去掉字符串的右边空格
'''
e =" hello "
f = e.rstrip()
print(f)

# 字符串大小写转换
'''
S.upper() #S中的字母大写
S.lower() #S中的字母小写
S.capitalize() #首字母大写
S.isupper() #S中的字母是否全是大写
S.islower() #S中的字母是否全是小写
S.istitle() #S中字符串中所有的单词拼写首字母是否为大写，且其他字母为小写
'''
g = "DREAMyee"
print(g.isupper())

# join拼接字符串
m = 'www.itdiffer.com'
n = m.split(".")
print (n)
i = ".".join(n)
print(i)
j = "*".join(n)
print(j)