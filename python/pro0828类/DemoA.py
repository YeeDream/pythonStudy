# -*-coding:utf-8 -*-
# *-*Author:DreamYee*-*
# Create:2019/08/28 17:52
# File:DemoA.py

# 继承
__metaclass__ = type
class Person:
    def speak(self):print("I love you.")
    def setHeight(self):print("The height is:1.60m.")
    def breast(self, n):print("My breast is:",n)
class Girl(Person):
        def setHeight(self):print("The height is:1.70m.")
if __name__ == "__main__":cang = Girl()
print(cang.setHeight())
print(cang.speak())
print(cang.breast(90))

# 多重继承
__metaclass__ = type
class Person:
    def eye(self):print("two eyes")
    def breast(self, n):print("The breast is:",n)
class Girl:
    age = 28
    def color(self):print("The girl is white")
class HotGirl(Person, Girl):
    pass
if __name__ == "__main__":kong = HotGirl()
print(kong.eye)
print(kong.breast(90))
print(kong.color())
print(kong.age)

# 多重继承：深度继承

# super()函数
__metaclass__ = type
class Person:
    def __init__(self):self.height = 160
    def about(self, name):print("{} is about {}.".format(name, self.height))
class Girl(Person):
    def __init__(self): super(Girl, self).__init__, self.breast = 90
    def about(self, name): print("{} is a hot girl, she is about {}, and her breast is {}".format(name, self.height, self.breast, super(Girl, self).about(name)))
if __name__ == "__main__": cang = Girl()
print(cang.about("canglaoshi"))
