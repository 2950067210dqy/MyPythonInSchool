# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 09:51:32 2021

@author: hasee
"""
import matplotlib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_boston

#1.使用sklearn调波士顿房价的数据集P74
d=load_boston()
feature=d.data
price=d.target
#2.查看波士顿房价数据集把取出DATA数据
data=pd.DataFrame(d.data,columns=d.feature_names)
#3.合并DATA和target的数据
# np 和 pd

price=price.reshape(506,1)
data1=np.concatenate((feature,price),axis=1)
data['price']=d.target
#4.把data和target的数据加入列名，英文一个，中文一个（不超过4个汉字）P144
name=d.feature_names
names=list(np.zeros(len(name)))
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
data2=pd.DataFrame(d.data)
data2.columns=names
data2['房价']=d.target
# data1=pd.DataFrame(d.data,columns=['犯罪率'，'非住宅'])        
#5.画相关性矩阵np.corrcoef(data, rowvar=False)，打印出与最能影响房价的4个特征
corr=np.corrcoef(data, rowvar=False)
pcorr=corr[:,-1]
pcorr=np.abs(pcorr)
pcorr=pd.DataFrame(pcorr)
pcorr1=pcorr.sort_values(by=0)
b=pcorr1.index
b=np.array(b)
b1=b[-5:-1]
b2=np.zeros(len(b1))
b2=list(b2)
b3=list(np.zeros(len(b1)))
for i in range(len(b1)):
    b3[i]=name[b1[i]]
for i in range(len(b1)):
    b2[i]=names[b1[i]]
    
#b2[0]=names[b1[0]=2]
#b2[1]=names[b1[1]=10]
#b2[2]=names[b1[2]=5]
#b2[3]=names[b1[3]=12]
    
#1.先把房价相关的那一列（最后一列）
#2.相关一列绝对值，然后排序
#3.排序后的索引取出来（对应特证名print）
#4.2个最相关的特征与class相关性
    
#6.画相关性分析图，把每一个特征维度与价格的相
#关性画出来，因为特征维度是13维的为了好看丢掉
#相关性最差的那个属性，然后画（3,4）的图
#fig=plt.figure(figsize=(10,7))
#ax1=fig.add_subplot(2,2,1)
#plt.ylabel('price')
#ax1.scatter(feature[:,2],price,label=name[2])
#plt.legend()
#ax2=fig.add_subplot(2,2,2)
#plt.ylabel('price')
#ax2.scatter(feature[:,10],price,label=name[10])
#plt.legend()
#ax3=fig.add_subplot(2,2,3)
#plt.ylabel('price')
#ax3.scatter(feature[:,5],price,label=name[5])
#plt.legend()
#ax4=fig.add_subplot(2,2,4)
#plt.ylabel('price')
#ax4.scatter(feature[:,12],price,label=name[12])
#plt.legend()
#plt.show()
fig=plt.figure(figsize=(10, 7))
#title
for i in range(len(b1)):
    ax=fig.add_subplot(2,2,i+1)
    plt.ylabel('prices')
    ax.scatter(data[b3[i]],price,label=name[i])
    plt.legend()
fig.suptitle('corr',fontsize=20)
plt.show()