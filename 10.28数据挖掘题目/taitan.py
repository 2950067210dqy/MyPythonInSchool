# -*- coding: utf-8 -*-
"""
Created on Thu Nov 18 15:41:16 2021

@author: Administrator
"""

#调包
import numpy as np
import pandas as pd
#导入数据集
features= pd.read_csv('C:/Util/titanic_dataset.csv')
#把标签和特征分开
y_train1=features['Survived']
X_train=features.drop('Survived',axis=1)
#获得特征的大小
(a,b)=X_train.shape
#获得标签的长度
a1=y_train1.shape
#查看特征集的缺失值情况
X_train.info()
# 缺失值合计
X_train.isnull().sum()
y_train1.isnull().sum()
# 待处理的缺失值
#X_train.Age
# X_train.Cabin
# X_train.Embarked
# X_train.Fare
import seaborn as sns
import matplotlib.pyplot as plt
plt.rcParams['font.family'] = ['SimHei']
fig1=plt.figure()

ax=fig1.add_subplot(2,2,1)
plt.title('原数据集')

# 先看下数据集的 Age 分布状态
sns.distplot(X_train['Age'].dropna(), hist=True, kde=True,axlabel=None)

# 将数据集中的NaN数据使用中值填充。
Xtrain1=X_train.copy()
#np.nanmedian沿指定轴计算中位数，而忽略NaN。
Xtrain1['Age'].replace(np.nan, np.nanmedian(Xtrain1['Age']),inplace=True)

#sns.distplot(Xtrain1['Age'].dropna(), hist=True, kde=True)
#性别有关的中位数
age_sex_median=X_train.groupby('Sex').Age.median()
Xtrain2=X_train.set_index('Sex')
Xtrain2.Age.fillna(age_sex_median,inplace=True)
Xtrain2.reset_index(inplace=True)
Xage2=Xtrain2['Age']
#同时考虑性别和仓位
age_Pclass=X_train.groupby(['Pclass','Sex']).Age.median()
X_train.set_index(['Pclass','Sex'],inplace=True)
X_train.Age.fillna(age_Pclass,inplace=True)
X_train.reset_index(inplace=True)

meanage=[[],[],[]]
meanage[0]=X_train.Age.mean()
meanage[1]=Xtrain1.Age.mean()
meanage[2]=Xtrain2.Age.mean()
ax=fig1.add_subplot(2,2,2)
plt.title('同时考虑性别和仓位')

sns.distplot(X_train['Age'], hist=True, kde=True)
ax=fig1.add_subplot(2,2,3)
plt.title('性别中位数')

sns.distplot(Xtrain1['Age'], hist=True, kde=True)
ax=fig1.add_subplot(2,2,4)
plt.title('中位数')
plt.xlabel('')
sns.distplot(Xtrain2['Age'], hist=True, kde=True)
plt.subplots_adjust(wspace=0,hspace=0.5)
plt.show()

X_train.drop("Cabin",axis=1,inplace=True)
X_train.Embarked.value_counts()
fig5=plt.figure()
fig5=sns.countplot(x='Embarked',data=X_train)

X_train['Embarked'].replace(np.nan,'S',inplace=True)
X_train[np.isnan(X_train['Fare'])]
pclass3_fares=X_train.query('Pclass==3 & Embarked =="S"')['Fare']
X_train['Embarked'].replace(['S','C','Q'],[1,2,3],inplace=True)

pclass3_fares=pclass3_fares.replace(np.nan,0)
median_fare=np.median(pclass3_fares)
X_train.loc[X_train['PassengerId']==1044,'Fare']=median_fare
X_train.loc[X_train['PassengerId']==1044]
X_train['Sex'].replace(['male','female'],[1,0],inplace=True)
X_train.isnull().sum()

data=X_train.drop('Name',axis=1)
data.drop('Ticket',axis=1,inplace=True)
#data.drop('PassengerId',axis=1,inplace=True)

from sklearn import  preprocessing
from sklearn.decomposition import PCA
# mms=preprocessing.MinMaxScaler()

# data=mms.fit_transform(data)
pca=PCA()
X_pca=pca.fit_transform(data)
ratio=pca.explained_variance_ratio_


from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import time
X_train,X_test,y_train,y_test=train_test_split(data,y_train1,test_size=0.1,random_state=50)

start=time.time()
knn=KNeighborsClassifier(n_neighbors=10)
knn.fit(X_train,y_train)
knn_score=knn.score(X_test,y_test)

end=time.time()
knn_time=end-start

from sklearn import svm
start=time.time()
clf=svm.SVC(kernel='linear')
clf.fit(X_train,y_train)
svm_score=clf.score(X_test,y_test)

end=time.time()
svm_time=end-start



plt.show()