# -*-coding:utf-8 -*-
# *-*Author:DreamYee*-*
# Create:2019/09/01 15:46
# File:DemoC.py

# XML
'''
XML 指可扩展标记语言（EXtensible Markup Language）
XML 是一种标记语言，很类似 HTML
XML 的设计宗旨是传输数据，而非显示数据
XML 标签没有被预定义。您需要自行定义标签。
XML 被设计为具有自我描述性。
XML 是 W3C 的推荐标准
'''

# 遍历查询
import xml.etree.cElementTree as ET
tree = ET.ElementTree(file="22601.xml")
print(tree)
root = tree.getroot()  # 获得根
print(root.tag)
print(root.attrib)
for child in root:
    print(child.tag,child.attrib)

for ele in tree.iter():
    print(ele.tag,ele.attrib)

# 编辑
import os
outpath = os.getcwd()
file = outpath+"/22601.xml"
tree.write(file)

# 常用属性和方法总结
'''
Element对象：
tag：string，元素数据种类
text：string，元素的内容
attrib：dictionary，元素的属性字典
tail：string，元素的尾形

clear()：清空元素的后代、属性、text和tail也设置为None
get(key, default=None)：获取key对应的属性值，如该属性不存在则返回default值
items()：根据属性字典返回一个列表，列表元素为(key, value）
keys()：返回包含所有元素属性键的列表
set(key, value)：设置新的属性键与值

append(subelement)：添加直系子元素
extend(subelements)：增加一串元素对象作为子元素
find(match)：寻找第一个匹配子元素，匹配对象可以为tag或path
findall(match)：寻找所有匹配子元素，匹配对象可以为tag或path
findtext(match)：寻找第一个匹配子元素，返回其text值。匹配对象可以为tag或path
insert(index, element)：在指定位置插入子元素
iter(tag=None)：生成遍历当前元素所有后代或者给定tag的后代的迭代器
iterfind(match)：根据tag或path查找所有的后代
itertext()：遍历所有后代并返回text值
'''
# 一个实例
from xml.etree.ElementTree import ElementTree,Element
def read_xml(in_path):
    ''' 读取并解析xml文件 in_path: xml路径 return: ElementTree '''
    tree = ElementTree()
    tree.parse(in_path)
    return tree
def write_xml(tree, out_path):
    ''' 将xml文件写出 tree: xml树 out_path: 写出路径 '''
    tree.write(out_path, encoding="utf-8",xml_declaration=True)
def if_match(node, kv_map):
    ''' 判断某个节点是否包含所有传入参数属性 node: 节点 kv_map: 属性及属性值组成的map '''
    for key in kv_map:
        if node.get(key) != kv_map.get(key):
            return False
            return True
#---------------search -----
def find_nodes(tree, path):
    ''' 查找某个路径匹配的所有节点 tree: xml树 path: 节点路径 '''
    return tree.findall(path)
def get_node_by_keyvalue(nodelist, kv_map):
    ''' 根据属性及属性值定位符合的节点，返回节点 nodelist: 节点列表 kv_map: 匹配属性及属性值map '''
    result_nodes = []
    for node in nodelist:
        if if_match(node, kv_map):
            result_nodes.append(node)
            return result_nodes
#---------------change -----
def change_node_properties(nodelist, kv_map, is_delete=False):
    ''' 修改/增加 /删除 节点的属性及属性值 nodelist: 节点列表 kv_map:属性及属性值map '''
    for node in nodelist:
        for key in kv_map:
            if is_delete:
                if key in node.attrib:
                    del node.attrib[key]
                else: node.set(key, kv_map.get(key))
def change_node_text(nodelist, text, is_add=False, is_delete=False):
    ''' 改变/增加/删除一个节点的文本 nodelist:节点列表 text : 更新后的文本 '''
    for node in nodelist:
        if is_add:
            node.text += text
        elif is_delete: node.text = ""
        else: node.text = text
def create_node(tag, property_map, content):
    ''' 新造一个节点 tag:节点标签 property_map:属性及属性值map content: 节点闭合标签里的文本内容 return 新节点 '''
    element = Element(tag, property_map)
    element.text = content
    return element
def add_child_node(nodelist, element):
    ''' 给一个节点添加子节点 nodelist: 节点列表 element: 子节点 '''
    for node in nodelist:
        node.append(element)
def del_node_by_tagkeyvalue(nodelist, tag, kv_map):
    ''' 同过属性及属性值定位一个节点，并删除之 nodelist: 父节点列表 tag:子节点标签 kv_map: 属性及属性值列表 '''
        for parent_node in nodelist:
            children = parent_node.getchildren()
            for child in children:
                if child.tag == tag and if_match(child, kv_map):
                    parent_node.remove(child)
if __name__ == "__main__":
# 1. 读取xml文件
    tree = read_xml("./test.xml")
#2. 属性修改
#   #A. 找到父节点
nodes = find_nodes(tree, "processers/processer")
#B. 通过属性准确定位子节点
result_nodes = get_node_by_keyvalue(nodes, {"name":"BProcesser"})
#C. 修改节点属性
change_node_properties(result_nodes, {"age": "1"})
#D. 删除节点属性
change_node_properties(result_nodes, {"value":""}, True)
#3. 节点修改
#A.新建节点
a = create_node("person", {"age":"15","money":"200000"}, "this is the firest content")
#B.插入到父节点之下
add_child_node(result_nodes, a)
#4. 删除节点
#定位父节点
del_parent_nodes = find_nodes(tree, "processers/services/service")
#准确定位子节点并删除之
target_del_node = del_node_by_tagkeyvalue(del_parent_nodes, "chain", {"sequency" : "chain1"})
#5. 修改节点文本
#定位节点
text_nodes = get_node_by_keyvalue(find_nodes(tree, "processers/services/service/chain"), {"sequency":"chain3"})
change_node_text(text_nodes, "new text")
#6. 输出到结果文件
write_xml(tree, "./out.xml")
