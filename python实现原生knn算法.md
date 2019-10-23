本文参考：https://blog.csdn.net/tanak/article/details/84380362
# pyhton实现knn算法
一.算法设计
	
1.knn算法介绍
	
KNN的原理就是当预测一个新的值x的时候，根据它距离最近的K个点是什么类别来判断x属于哪个类别。
	
2.**knn算法描述**

对需要分类的点依次执行以下操作：

    a.计算已知类别数据集中每个点与该点之间的距离
	
    b.按照距离递增顺序排序
		
    c.选取与该点距离最近的k个点
		
    d.确定前k个点所在类别出现的频率
	
    e.返回前k个点出现频率最高的类别作为该点的预测分类

3.流程图

![在这里插入图片描述](https://img-blog.csdnimg.cn/20191014143107513.png)

二.源代码

1.获取鸢尾花的数据集

```python
from sklearn import datasets
from sklearn.model_selection import train_test_split
iris = datasets.load_iris()
X = iris.data
y = iris.target
#拆分训练集、测试集
#X特征的二维数组：包含数据，每个数据点对应一行，每个特征对应一列
#y一维数组：类别标签
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25)
print(X_train[0:40])
print(y_train[0:40])
print(X_test[0:40])
print(y_test[0:40])
```
2.==knn算法==(重点代码)

```python
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
```
3.创建knn对象，测试：

```python
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
```
三.测试用例设计及调试过程

1.数据集：

这里只截取了部分数据：(*这里所使用的编译器是pycharm*)

![在这里插入图片描述](https://img-blog.csdnimg.cn/20191014143448738.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NDY5NDMxNw==,size_16,color_FFFFFF,t_70)

![](https://img-blog.csdnimg.cn/2019101414350839.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NDY5NDMxNw==,size_16,color_FFFFFF,t_70)

![在这里插入图片描述](https://img-blog.csdnimg.cn/20191014143521472.png)

2.当k=3时，结果：(*这里使用的是Jupyter编译器*)

![在这里插入图片描述](https://img-blog.csdnimg.cn/20191014143542690.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NDY5NDMxNw==,size_16,color_FFFFFF,t_70)

3.当k=5时，结果：

![在这里插入图片描述](https://img-blog.csdnimg.cn/20191014143605511.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NDY5NDMxNw==,size_16,color_FFFFFF,t_70)

四.总结

通过这次实验：从中总结了几点：

1.knn算法要计算欧氏距离：

![在这里插入图片描述](https://img-blog.csdnimg.cn/20191014210055642.png)

2.KNN做分类预测时，一般是选择多数表决法，即训练集里和预测的样本特征最近的K个样本，预测为里面有最多类别数的类别。

3.KNN算法我们主要要考虑三个重要的要素，对于固定的训练集，只要这三点确定了，算法的预测方式也就决定了。这三个最终的要素是k值的选取，距离度量的方式和分类决策规则。

4.==对于k值的选择==，没有一个固定的经验，一般根据样本的分布，选择一个较小的值，可以通过交叉验证选择一个合适的k值。
　　选择较小的k值，就相当于用较小的领域中的训练实例进行预测，训练误差会减小，只有与输入实例较近或相似的训练实例才会对预测结果起作用，与此同时带来的问题是泛化误差会增大，换句话说，K值的减小就意味着整体模型变得复杂，容易发生过拟合；
　　选择较大的k值，就相当于用较大领域中的训练实例进行预测，其优点是可以减少泛化误差，但缺点是训练误差会增大。这时候，与输入实例较远（不相似的）训练实例也会对预测器作用，使预测发生错误，且K值的增大就意味着整体的模型变得简单。(参考：https://www.cnblogs.com/zhengxingpeng/p/6670451.html)