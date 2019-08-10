# -*-coding:utf-8 -*-
# *-*Author:DreamYee*-*
# Create:2019/08/10 11:26
# File:DemoB字典.py

# 字典(dictionary)  dict
citys = ["suzhou", "tangshan", "shanghai"]
city_codes = ["0512", "0315", "011", "012"]
print("{}:{}".format(citys[0], city_codes[0]))

# int()  bin()  oct()  hex()

# 1.创建dict
# 方法一:键值对，键是唯一的，不能重复；值则是对应于键，可以重复
mydict = {}
person = {"name":"dream"}
print(person)
# 向dict中增加键值对的方法，字典可以原地修改，即是可变的
person['name2'] = "jackson"
print(person)

# 方法二：利用元组在建构字典
# ①
name = (["first", "Google"], ["second", "Yahoo"])
website = dict(name)
print(website)
# ②
ad = dict(name="dream", age=20)
print(ad)

# 方法三:使用fromkeys,这种方法是重新建立一个dict
website = {}.fromkeys(("third", "forth"), "facebook")
print(website)

# 访问dict的值
person = {"name": "dream"}
print(person['name'])
city_code = {"suzhou": "0512", "tangshan": "0315", "beijing": "011", "shanghai": "012"}
print(city_code["suzhou"])

# 基本操作
'''
len(d):返回字典(d)中的键值对的数量
d[key]:返回字典(d)中的键(key)的值
d[key]=value:将值(value)赋给字典(d)中的键(key)
del d[key]:删除字典(d)的键(key)项（将该键值对删除）
key in d:检查字典(d)中是否含有键为key的项
'''
print(len(city_code))
city_code = {'suzhou': '0512', 'beijing': '011', 'shanghai': '012', 'tangshan': '0315', 'nanjing': '025'}
# 删除  del
del city_code["shanghai"]
print(city_code)

# 字符串格式化输出
city_code = {"suzhou": "0512", "tangshan": "0315", "hangzhou": "0571"}
m = "Suzhou is a beautiful city,its area code is %(suzhou)s" % city_code
print(m)

temp = "<html><head><title>%(lang)s<title><body><p>My name is %(name)s.<p/></body></head></html>"
my = {"name": "dream", "lang": "python"}
n = temp % my
print(n)
