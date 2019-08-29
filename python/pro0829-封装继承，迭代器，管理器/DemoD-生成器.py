# -*-coding:utf-8 -*-
# *-*Author:DreamYee*-*
# Create:2019/08/29 16:22
# File:DemoD-生成器.py

# 简单的生成器
my_generator = (x*x for x in range(4))
my_list = [x*x for x in range(4)]
print(dir(my_generator))
for i in my_generator:
    print(i)
for i in my_list:
    print(i)

print(sum(i*i for i in range(10)))

# 定义和执行过程
def g():
    yield 0
    yield 1
    yield 2
print(g)
ge = g()
print(ge.__next__())
print(ge.__next__())
'''
yield的作用：就是在调用的时候返回相应的值
'''
# yield
def r_return(n):
    print("You taked me.")
    while(n>0):
        print("before return")
        return n
    n-=1
    print("after return")
rr = r_return(3)
print(rr)

def y_yield(n):
    print("You taked me.")
    while(n>0):
        print("before yield")
        yield n
    n-=1
    print("after yield")
yy = y_yield(3)
print(yy.__next__())
print(yy.__next__())
print(yy.__next__())
print(yy.__next__())
print(yy)

# 斐波那切数列
def fibs(max):
    n, a, b = 0, 0, 1
    while n<max:
        yield b
        a, b = b, a+b
        n = n+1
if __name__ =="__main__":
    f = fibs(10)
    for i in f:
        print(i)

# 生成器方法
def repeater(n):
    while True:
        n = (yield n)
r = repeater(4)
print(r.__next__())
print(r.send("hello"))

# throw(type, value = None, traceback = None):用于在生成器内部抛出一个异常
# close():调用时不用参数，用于关闭生成器