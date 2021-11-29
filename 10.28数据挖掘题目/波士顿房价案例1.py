# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 20:51:37 2021

@author: hasee
"""

#1.使用sklearn调波士顿房价的数据集P74
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import datasets
d=datasets.load_boston()
#2.查看波士顿房价数据集把取出DATA数据
data=pd.DataFrame(d.data)
#3.合并DATA和target的数据
data['price']=d.target
data.sample(5)
# 获取房屋价格
prices = data['price']
# 获取房屋特征
features = data.drop('price', axis=1) 
print("波士顿房屋数据有{}条 x {}列。".format(data.shape[0], data.shape[1]))
#4.把data和target的数据加入列名，英文一个，中文一个（不超过4个汉字）P144
#先做一个全0数组维度和feature_names的长度一致
a=d.feature_names.shape
name=np.zeros(a)
#把d.feature_names里面的变量赋给name
name=d.feature_names
#取Data的时候可以直接加列名
feature=pd.DataFrame(d.data,columns=name)
#dataset=pd.DataFrame(boston.data,
#                     columns=['犯罪率', '住宅用地', 
#                              '非住宅用地' ,'虚拟变量' ,
#                              '环保指数', '房间数' ,
#                              '自住单位','中心距离','便利指数',
#                              '不动产税率','师生比','黑人比例',
#                              '房东低收入'])

#把全0数组改成list
names=list(np.zeros(feature.shape[1]))
#names=pd.DataFrame(names)
for i in range(13):
    if name[i]=='CRIM':
        names[i]='犯罪率'
    if name[i]=='INDUS':
        names[i]='非住宅用地'
    if name[i]=='NOX':
        names[i]='环保指数'
    if name[i]=='AGE':
        names[i]='房龄'
    if name[i]=='RAD':
        names[i]='便利指数'
    if name[i]=='PTRATIO':
        names[i]='师生比'
    if name[i]=='LSTAT':
        names[i]='低收入'
    if name[i]=='ZN':
        names[i]='住宅用地'
    if name[i]=='CHAS':
        names[i]='虚拟变量'  
    if name[i]=='RM':
        names[i]='房间数' 
    if name[i]=='DIS':
        names[i]='就业距离' 
    if name[i]=='TAX':
        names[i]='不动产税率'   
    if name[i]=='B':
        names[i]='黑人比例'  
feature1=pd.DataFrame(d.data,columns=names)
#给已经变为DataFrame格式，改列名
features.columns=names 
#5.画相关性矩阵np.corrcoef(data, rowvar=False)，打印出与最能影响房价的4个特征
corr=np.corrcoef(data, rowvar=False)
#把房价的那一列相关系数取出来，并转化成DataFrame格式
b=pd.DataFrame(corr[:,data.shape[1]-1])
#取绝对值，因为负值越接近-1也越相关的
b=np.abs(b)
#排序第0列
b1=b.sort_values(by=0)
#取索引
b2=b1.index
b2=np.array(b2)
#取出最大的4位，要把第一个排除掉所以-1，
#因为相关矩阵里，最相似的是与其本身一样的值
b3=b2[b2.shape[0]-5:b2.shape[0]-1]
#弄一个4位的list用来装变量
b4=list(np.zeros(b3.shape[0]))
#循环给b4赋值
for i in range(4):
    b4[i]=str(names[b3[i]])
print(b4)
#6.画相关性分析图，把每一个特征维度与价格的相关性画出来，因为特征维度是13维的为了好看丢掉相关性最差的那个属性，然后画（3,4）的图
plt.rcParams['font.family'] = ['SimHei']    #用于画图时显示中文
features = features.drop('虚拟变量', axis=1) 
names.remove('虚拟变量')
fig=plt.figure(figsize=(10, 7))
for i in range(features.shape[1]):
    ax=fig.add_subplot(4,3,i+1)
    plt.ylabel('prices')
    ax.scatter(features[names[i]],prices,label=names[i])
    plt.legend()
fig.suptitle('各特征与价格的相关性',fontsize=20)
##选做，1.使用循环画图（还是相关性散点图）
#2.选取二个最能影响房价的特征，使用seaborn绘制二个回归图 P90
fig1=plt.figure()
import seaborn as sns
features=np.array(features)
# regplot()函数根据数据绘制线性回归（Linear Regression）模型图
sns.regplot(feature1['房间数'], prices, color='red')
# 显示绘图
plt.show()
fig2=plt.figure()
# regplot()函数根据数据绘制线性回归（Linear Regression）模型图
sns.regplot(feature1['低收入'], prices, color='green')
# 显示绘图
plt.show()