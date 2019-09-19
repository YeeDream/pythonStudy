# -*-coding:utf-8 -*-
# *-*Author:DreamYee*-*
# Create:2019/09/02 14:38
# File:DemoA.py

# pickle
import pickle
integers = [1,2,3,4,5]
f = open("22091.dat", "wb")
print(pickle.dump(integers, f))
f.close()

import pickle
d = {}
integers = range(9999)
d["i"] = integers
#下面将这个dict格式的对象存入文件
f = open("22902.dat", "wb")
pickle.dump(d, f)
#文件中以ascii格式保存数据
f.close()
f = open("22903.dat", "wb")
pickle.dump(d, f, True)
#文件中以二进制格式保存数据
f.close()
import os
s1 = os.stat("22902.dat").st_size
#得到两个文件的大小
s2 = os.stat("22903.dat").st_size
print("%d, %d, %.2f%%" % (s1, s2, (s2+0.0)/s1*100))

# shelve
import shelve
s = shelve.open("22901.db")
s["name"] ="www.baidu.com"
s["lang"] = "python"
s["pages"] = 1000
s["contents"] = {"first":"base language","second":"day day up"}
s.close()

