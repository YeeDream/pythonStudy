# -*-coding:utf-8 -*-
# *-*Author:DreamYee*-*
# Create:2019/09/23 22:18
# File:Graph-有向图.py

# 自定义有向图结构
def searchPath(graph,start,end):
    results = []
    _generatePath(graph,[start],end,results)
    results.sort(key=lambda x:len(x))  # 按所有路径的长度排队
    return results

def _generatePath(graph,path,end,results):
    current = path[-1]
    if current==end:
        results.append(path)
    else:
        for n in graph[current]:
            if n not in path:
                _generatePath(graph,path+[n],end,results)

def showPath(results):
    print('The path from',results[0][0],'to', results[0][-1], 'is:')
    for path in results:
        print(path)

if __name__=='__main__':
    graph={'A': ['B', 'C', 'D'],
           'B': ['E'],
           'C': ['D', 'F'],
           'D': ['B', 'E', 'G'],
           'E': ['D'],
           'F': ['D', 'G'],
           'G': ['E']}
    r1=searchPath(graph, 'A', 'D')
    showPath(r1)