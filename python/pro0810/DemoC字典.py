# -*-coding:utf-8 -*-
# *-*Author:DreamYee*-*
# Create:2019/08/10 14:11
# File:DemoC字典.py

# 字典方法
# copy
ad = {"name": "dream", "lang": "python"}
bd = {'lang': 'python', 'name': 'dream'}
cd = ad.copy()
print(cd)
cd["name"] = 'itdiffer.com'
print(cd)
print(ad)
bd["name"] = "laoqi"
print(ad)
print(bd)
x = {"name": "dream","lang":["python", "java", "c"]}
y = x.copy()
print(y)
print(id(x))
print(id(y))
# remove()：移除元素
y['lang'].remove("c")
print(y)
print(x)

# 深拷贝(deep copy):拷贝之后，不影响原来的字典
# copy.deepcopy(),需要导包
import copy
z = copy.deepcopy(x)
print(z)

# clear():清空字典中所有元素的操作
a = {"name": "dream"}
a.clear()
print(a)

# get,setdefault
# get():得到字典中某个键的值
d = {"lang": 'python'}
e= d.get("lang")
print(e)
print(d.get("name"))
# print(d["name"])
newd = d.get("name","dream")
print(newd)
print(d)
# D.setdefault(k):将增加的键值对添加到原来的字典中了，而get()没有这个功能
m = d.setdefault("lang")
print(m)
n = d.setdefault("name","dream")
print(n)
print(d)

# items/iteritems  keys/iterkeys   values/itervalues
# items(): 得到一个关于一个字典的列表
dd = {"name": "dream", "lang": "python", "web": "www.baidu.com"}
dd_kv = dd.items()
print(dd_kv)

dd_k = dd.keys()
print(dd_k)
dd_v = dd.values()
print(dd_v)

# pop  popitem
# 删除列表中元素的函数：pop()   remove()
#  pop([i]):用于删除指定索引的元素，如果不提供索引，就默认删除最后一个
#  remove()：用来删除指定的元素
m = dd.pop("name")
print(m)
print(dd)
dd = {"name": "dream", "lang": "python", "web": "www.baidu.com", "yee": "jackson"}
# popitem():一次随机删除一对键值对，并以一个元组的形式返回
n = dd.popitem()
print(dd)

# update():更新字典
d1 = {"lang": "python"}
d2 = {"song": "I dreamed a dream"}
d1.update(d2)
d2.update([("name","yee"),("web","www.baidu.com")])
print(d1)
print(d2)

# has_key():判断字典中是否存在某个键   与k  in  D类似
d2 = {'web': 'itdiffer.com', 'name': 'qiwsir', 'song': 'I dreamed a dream'}
print("web" in d2)
