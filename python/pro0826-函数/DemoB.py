# -*-coding:utf-8 -*-
# *-*Author:DreamYee*-*
# Create:2019/08/26 15:50
# File:DemoB.py

# 递归
def fib(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
if __name__ == "__main__":
    f = fib(10)
    print(f)

'''
几个特殊函数：
filter
map
reduce
lambda
yield
'''
def add(x):
    x += 3
    return x
numbers = range(10)
new_numbers = []
for i in numbers:
    new_numbers.append(add(i))
print(new_numbers)

lam = lambda x: x + 3
n2 = []
for i in numbers:
    n2.append(lam(i))
print(n2)
'''
lambda函数的使用方法：
在lambda后面直接跟变量
变量后面是冒号
冒号后面是表达式，表达式结果就是本函数的返回值
'''

numbers = [0,1,2,3,4,5,6,7,8,9]
map(add,numbers)
print(map(lambda x:x+3,numbers))
'''
map()函数的用法：
对iterable中的每个元素，依次应用function的方法
将所有结果返回一个list
如果参数很多，则对那些参数并行执行function
'''

# filter   过滤器
for i in range(-5,5):
    print(numbers[i])
