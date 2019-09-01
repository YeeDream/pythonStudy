# -*-coding:utf-8 -*-
# *-*Author:DreamYee*-*
# Create:2019/09/01 13:52
# File:DemoB.py

# urllib 用于读取来自网上的数据
import urllib
# itdiffer = urllib.urlopen("https://www.baidu.com")
# print(itdiffer.read())
# urlopen():用于打开url文件，然后就获得指定的url数据
'''
url：远程数据的路径，常常是网址
data：如果使用post方式，这里就是所提交的数据
proxies：设置代理
read(),readline(),readlines(),fileno(),close()：都与文件操作一样，这里不再赘述。可以参考前面有关文件章节
info()：返回头信息
getcode()：返回http状态码
geturl()：返回url
'''
# print(itdiffer.info())

# 对url编码，解码
'''
quote(string[, safe])：对字符串进行编码。参数safe指定了不需要编码的字符
urllib.unquote(string) ：对字符串进行解码
quote_plus(string [ , safe ] ) ：与urllib.quote类似，但这个方法用'+'来替换空格' '，而quote用'%20'来代替空格
unquote_plus(string ) ：对字符串进行解码；
urllib.urlencode(query[, doseq])：将dict或者包含两个元素的元组列表转换成url参数。例如{'name': 'laoqi', 'age': 40}将被转换为"name=laoqi&age=40"
pathname2url(path)：将本地路径转换成url路径
url2pathname(path)：将url路径转换成本地路径
'''
import urllib
du ="https://www.itdiffer.com/name=python book"
print(urllib.quote(du))
print(urllib.quote_plus(du))

# urlretrieve()建立类文件对象

# Request类
import urllib3
req = urllib3.Request("https://www.baidu.com")
