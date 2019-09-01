# -*-coding:utf-8 -*-
# *-*Author:DreamYee*-*
# Create:2019/09/01 17:14
# File:DemoD.py

# json
# 基本操作
import json
print(json.__all__)

data = {"name":"dream","lang":("python","english"),"age":40}
print(data)
data_json = json.dumps(data)
print(data_json)
print(type(data_json))
print(type(data))

# 大json字符串
import tempfile
f = tempfile.NamedTemporaryFile(mode="w+")
json.dump(data,f)
f.flush()
print(open(f.name, "r").read())
