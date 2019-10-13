# -*-coding:utf-8 -*-
# *-*Author:DreamYee*-*
# Create:2019/10/10 22:25
# File:Knn.py


import numpy as np
import pandas as pd

# 鸢尾花数据集中包含两个数组：
# 一个包含数据：二维数组，每个数据点对应一行，每个特征对应一行
# 一个包含正确的输出或预期输出：一维数组，包含一个类别标签

# 定义KNN类，用于分类，类中定义两个预测方法，分为考虑权重不考虑权重两种情况
class KNN:
    ''' 使用Python语言实现K近邻算法。（实现分类） '''
    def __init__(self, k):
        '''
        初始化方法
           Parameters
           -----
           k:int 邻居的个数
        '''
        self.k = k

    def fit(self, X, y):
        '''训练方法
            Parameters
            ----
            X : 类数组类型，形状为：[样本数量, 特征数量]
            待训练的样本特征（属性）

        y : 类数组类型，形状为： [样本数量]
            每个样本的目标值（标签）。
        '''
        # 将X转换成ndarray数组
        self.X = np.asarray(X)
        self.y = np.asarray(y)

    def predict(self, X):
        """
        根据参数传递的样本，对样本数据进行预测。
        Parameters
        -----
        X : 类数组类型，形状为：[样本数量, 特征数量]
            待训练的样本特征（属性）
        Returns
        -----
        result : 数组类型
            预测的结果。
        """
        X = np.asarray(X)
        result = []
        # 对ndarray数组进行遍历，每次取数组中的一行。
        for x in X:
            # 求欧氏距离：对于测试集中的每一个样本，依次与训练集中的所有样本求距离。
            dis = np.sqrt(np.sum((x - self.X) ** 2, axis=1))
            ## 返回数组排序后，每个元素在原数组（排序之前的数组）中的索引。
            index = dis.argsort()
            # 进行截断，只取前k个元素。[取距离最近的k个元素的索引]
            index = index[:self.k]
            # 返回数组中每个元素出现的次数。元素必须是非负的整数。[使用weights考虑权重，权重为距离的倒数。]
            count = np.bincount(self.y[index], weights=1 / dis[index])
            # 返回ndarray数组中，值最大的元素对应的索引。该索引就是我们判定的类别。
            # 最大元素索引，就是出现次数最多的元素。
            result.append(count.argmax())
        return np.asarray(result)

'''
#创建KNN对象，进行训练与测试。
knn = KNN(k=3)
#进行训练
knn.fit(X_train, y_train)
#进行测试
result = knn.predict(X_test)
# display(result)
# display(test_y)
display(np.sum(result == y_test))
display(np.sum(result == y_test)/ len(result))
'''

