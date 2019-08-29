# -*-coding:utf-8 -*-
# *-*Author:DreamYee*-*
# Create:2019/08/29 16:46
# File:DemoE-上下文管理器.py

# __enter__()     __exit__()
name = "dream"
if name == "dream":
    print(name)
if name == "dream":
    for i in name:
        print(i)
f = open("a.txt", "w")
f.write("hello")
f.write("python")
f.close()

read_file = open("E:\\upload\\23501.txt")
write_file = open("E:\\upload\\23501.txt","w")
try:
    r = read_file.readlines()
    for line in r:
        write_file.write(line)
finally:
    read_file.close()
    write_file.close()


class ContextManagerOpenDemo(object):
    def __init__(self, filename, mode): self.filename = filename, self.mode = mode
    def __enter__(self): self.open_file = open(self.filename, self.mode), print("Starting the Manager.")
    def __exit__(self, *others): self.open_file.close(), print("Exiting the Manager.")
    with ContextManagerOpenDemo("E:\\upload\\23501.txt", 'r') as reader: print("In the Manager.")
    for line in reader:
        print(line)

# contextlib模块
import contextlib
'''
contextlib.closing()
contextlib.nested()
contextlib.contextmanager
'''

