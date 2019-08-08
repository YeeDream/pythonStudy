# Author:DreamYee
# Create:2019/08/08 13:50
# File:DemoE字符编码.py

# 编码：ASCII    Unicode    UTF-8
'''
ASCII:ASCII（pronunciation:
英语发音：/ˈæski/ ASS-kee[1]，American Standard Code for Information Interchange，美国信息交换标准代码）
是基于拉丁字母的一套电脑编码系统。
它主要用于显示现代英语，而其扩展版本EASCII则可以部分支持其他西欧语言，并等同于国际标准ISO/IEC 646。
由于万维网使得ASCII广为通用，直到2007年12月，逐渐被Unicode取代。

Unicode:Unicode（中文：万国码、国际码、统一码、单一码）
是计算机科学领域里的一项业界标准。
它对世界上大部分的文字系统进行了整理、编码，使得电脑可以用更为简单的方式来呈现和处理文字。

UTF-8:UTF-8（8-bit Unicode Transformation Format）是一种针对Unicode的可变长度字符编码，也是一种前缀码。
它可以用来表示Unicode标准中的任何字符，且其编码中的第一个字节仍与ASCII兼容，这使得原来处理ASCII字符的软件无须或只须做少部份修改，即可继续使用。
因此，它逐渐成为电子邮件、网页及其他存储或发送文字的应用中，优先采用的编码。
'''

# encode与decode
# encode:编码     decode:解码
a = "中"
print(a)
print(type(a))

# 如何防止乱码
# 在开头声明：# -*-coding:utf-8 -*-
