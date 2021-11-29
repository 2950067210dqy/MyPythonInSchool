# # -*- coding: utf-8 -*-
# """
# Created on Mon Oct 25 10:34:42 2021
#
# @author: 龚敏
# """
#
# # -*- coding: utf-8 -*-
# """
# Created on Wed Oct 13 20:51:37 2021
#
# @author: hasee
# """
#
# #1.使用sklearn调iris的数据集P74
# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt
# from sklearn import datasets
# from sklearn.datasets import load_iris #导入数据集iris
# iris=load_iris()
# #2.查看iris数据集把取出DATA数据
# data=pd.DataFrame(iris.data)
# #3.合并DATA和target的数据
# data['irisclass']=iris.target
# # 获取class
# irisclass = data['irisclass']
# # 获取花朵特征
# features = data.drop('irisclass', axis=1)
# print("花朵数据有{}条 x {}列。".format(data.shape[0], data.shape[1]))
# #4.加列名
# #先做一个全0数组维度和feature_names的长度一致
# #把iris.feature_names里面的变量赋给name
# name=iris.feature_names
# #取Data的时候可以直接加列名
# feature=pd.DataFrame(iris.data,columns=name)
# #把全0数组改成list
# names=list(np.zeros(feature.shape[1]))
# for i in range(4):
#     if name[i]=='sepal length (cm)':
#         names[i]='花萼长度'
#     if name[i]=='sepal width (cm)':
#         names[i]='花萼宽度'
#     if name[i]=='petal length (cm)':
#         names[i]='花瓣长度'
#     if name[i]=='petal width (cm)':
#         names[i]='花瓣宽度'
# feature1=pd.DataFrame(iris.data,columns=names)
# #给已经变为DataFrame格式，改列名
# features.columns=names
#
#
#
#
#
# #5.画相关性矩阵np.corrcoef(data, rowvar=False)，打印出与最能影响花朵的2个特征
# corr=np.corrcoef(data, rowvar=False)
# #把花朵的那一列相关系数取出来，并转化成DataFrame格式
# b=pd.DataFrame(corr[:,data.shape[1]-1])
# #取绝对值，因为负值越接近-1也越相关的
# b=np.abs(b)
# #排序第0列
# b1=b.sort_values(by=0)
# #取索引，转化为数组
# b2=b1.index
# b2=np.array(b2) #转换为数组
# #取出最大的4位，要把第一个排除掉所以-1，
# #因为相关矩阵里，最相似的是与其本身一样的值
# b3=b2[b2.shape[0]-3:b2.shape[0]-1]
# #弄一个2位的list用来装变量
# b4=list(np.zeros(b3.shape[0]))
# #循环给b4赋值
# for i in range(2):
#     b4[i]=str(names[b3[i]])
# print(b4)
#
#
#
#
#
#
#
# #6.画相关性分析图，把每一个特征维度与价格的相关性画出来，因为特征维度是13维的为了好看丢掉相关性最差的那个属性，然后画（3,4）的图
# plt.rcParams['font.family'] = ['SimHei']    #用于画图时显示中文
# fig=plt.figure(figsize=(10, 7))
# for i in range(2):
#     ax=fig.add_subplot(2,2,i+1)
#     plt.ylabel('irisclass')
#     ax.scatter(features[b4[i]],irisclass,label=b4[i])
#     plt.legend()
# fig.suptitle('与irisclass最相关的两个特征',fontsize=20)
# ##选做，1.使用循环画图（还是相关性散点图）
# #2.选取二个最能影响花朵的特征，使用seaborn绘制二个回归图 P90
# fig1=plt.figure()
# import seaborn as sns
# features=np.array(features)
# # regplot()函数根据数据绘制线性回归（Linear Regression）模型图
# sns.regplot(feature1[b4[0]], irisclass, color='red')
# # 显示绘图
# plt.show()
#
#
# fig2=plt.figure()
# # regplot()函数根据数据绘制线性回归（Linear Regression）模型图
# sns.regplot(feature1[b4[1]], irisclass, color='green')
# # 显示绘图
# plt.show()
#




import re
text="i have many issouiition"
print(re.sub(r"i","I",text))





















