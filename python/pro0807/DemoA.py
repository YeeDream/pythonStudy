# Author:DreamYee
# Create:2019/08/07 11:15
# File:DemoA.py
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