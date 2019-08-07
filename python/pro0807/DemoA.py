# Author:DreamYee
# Create:2019/08/07 11:15
# File:DemoA.py
import math

# 基本运算：+
i = 4+2.0
print(i)

# 简单的if语句
the_world_is_float = 1
if the_world_is_float:
    print("Be careful not to fall off!")

# 对象有类型，变量无类型。
# 看变量属于哪一种类型？
print(type(i))

# 不管是被除数还是除数，只要有一个数是浮点数，结果就是浮点数。
m = 9/2.0
print(m)

n = 10.0/3
print(n)

# divmod()函数返回了商和余数
y = divmod(5, 2)
print(y)

# round()函数进行四舍五入（逗号后面是保留几位数）
x = round(1.235, 2)
print(x)

# 常用数学函数及运算优先级  模块：Math
a = math.pi
print(a)
b = math.sqrt(9)  # 开方
c = math.pow(4, 2)  # 等同于4**2  幂次方
d = math.floor(3.14)  # 向下取整
e = math.floor(3.93)  # 同上
f = math.fabs(-2)   # 绝对值 等同于abs(-2)
g = math.fmod(5, 3)  # 等同于5%3

# q求绝对值
h = abs(-1.4)
# 四舍五入
j = round(1.234)  # result:1.0
k = round(1.234, 2)  # result:1.23

# 运算优先级
'''
运算符        描述
lambda       Lambda表达式
or           布尔“或”
and          布尔“与”
not x        布尔“非”
in,not in    成员测试
is,is not    同一性测试
<,<=,>,>=,!=,==比较
\            按位或
^            按位异或
&            按位与
<<,>>        移位
+，-，*，/，% 加减乘除余
+x,-x       正负号
~x          按位翻转
**          指数
x.attribute 属性参考
x[index]    下标
f(arguments...)函数调用
{key:datum,..} 字典显示
[expression,...]列表显示
'expression,..'字符串转换
       
'''