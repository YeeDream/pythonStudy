# Author:DreamYee
# Create:2019/08/08 13:48
# File:DemoA字符串.py

#  用单引号和双引号结果一样
a = 250
b = '250'
c = "250"
print(type(a))
print(type(b))
print(type(c))

# 对于一句话中有单引号的，我们采用以下方法：
# 1.双引号包裹单引号,也可以单引号包裹双引号，或者二者嵌套都可以
c = "What's your name?"
print(c)

# 2.使用转义符\
d = 'What\'s your name?'
print(d)
'''
转义字符           描述
\                 (在行尾时)续行符
\                 反斜杠符号
\'                单引号
\"                双引号
\a                响铃
\b                退格（backspace）
\e                转义
\000              空
\n                换行
\v                纵向制表符
\t                横向制表符
\r                回车
\f                换页
\oyy              八进制数，yy代表的字符，例如：\o12代表换行
\ xyy             十六进制数，例：\x0a代表换行
\other            其他的字符以普通格式输出
'''

# 拼接字符串
# 1.用+将两种同类型的字符串连接起来
e = "py"+"thon"
print(e)

# 2.str(x)将整数对象转化为字符串对象
f = 1989
g = "free"
print(g+str(f))
# 3.repr(x)：一个函数，反引号的替代品，能够把结果字符串转化为合法的python表达式。
print(g+repr(f))
