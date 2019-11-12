# -*-coding:utf-8 -*-
# *-*Author:DreamYee*-*
# Create:2019/11/12 16:42
# File:ProgramObject.py

'''
1. 创建SchoolMem类，该类中包含三种属性：姓名、性别、年龄以及针对每个属性的get和set方法；
2. 创建Student类，继承自SchoolMem类，添加额外三个属性：班级、学号和数量统计。
3. 创建Teacher类，继承自SchoolMem类，添加额外三个属性：科室、工号和数量统计。
4. 要求在Student类和Teacher类中分别实现printInfo方法，该方法打印对象的多有属性信息。
'''
# SchoolMeM类
class SchoolMem:
    def __init__(self,name,sex,age):  # 三个属性
        self.__name=name
        self.__sex=sex
        self.__age=age
    # name的get,set方法
    def __getName(self):
          return self.__name
    def __setName(self, name):
        self.__name = name

    # sex的get,set方法
    def __setSex(self, sex):
        self.__sex = sex
    def __getSex(self):
        return self.__sex

    # age的get,set方法
    def __getAge(self):
        return self.__age
    def __setAge(self, age):
        self.__age=age

    def printInfo(self):
        print("姓名：", self.__name)
        print("性别：", self.__sex)
        print("年龄：", self.__age)

# 类Student继承SchoolMem
class Student(SchoolMem):
    def __init__(self,name,sex,age,classes,number,count):
        # 父类的三个属性与子类的三个属性
        super(Student,self).__init__(name,sex,age)
        self.__classes=classes
        self.__number=number
        self.__count=count

    def printInfoS(self):
        super(Student,self).printInfo()
        print("班级：",self.__classes)
        print("学号：",self.__number)
        print("数量统计：",self.__count)

# 类Teacher继承SchoolMem类
class Teacher(SchoolMem):
    def __init__(self,name,sex,age,dept,no,sum):
        # 父类的三个属性与子类的三个属性
        super(Teacher, self).__init__(name, sex, age)
        self.__dept=dept
        self.__no=no
        self.__sum=sum
    def printInfoT(self):
        super(Teacher,self).printInfo()
        print("科室：",self.__dept)
        print("工号：",self.__no)
        print("数量统计：",self.__sum)

# 主函数
if __name__=='__main__':
    stu1=Student('zhangsan','man',18,'软工1','1101',2)
    stu1.printInfoS()
    print("======================")
    tea1=Teacher('Mr.Wang','man',36,'信计','1034',5)
    tea1.printInfoT()