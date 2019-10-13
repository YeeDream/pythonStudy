# -*-coding:utf-8 -*-
# *-*Author:DreamYee*-*
# Create:2019/10/11 17:19
# File:knn2.py

from sklearn import datasets
from sklearn.model_selection import train_test_split

iris = datasets.load_iris()
X = iris.data
y = iris.target
'''
print(X[0:10])
print(y[0:150])
print(iris.DESCR)
'''

# 拆分训练集、测试集
#  X特征的二维数组：包含数据，每个数据点对应一行，每个特征对应一列
#  y一维数组：类别标签
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25)
print(X_train[0:40])
print("=========")
print(y_train[0:40])
print("=========")
print(X_test[0:40])
print("=========")
print(y_test[0:40])
print("=========")

'''
# 特征工程（标准化）
std = StandardScaler()
X_train = std.fit_transform(X_train)
X_test = std.transform(X_test)
print(X_train[0:40])
'''

