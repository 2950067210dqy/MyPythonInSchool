import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#导入数据集
features=pd.read_csv('C:/StudyDocument/titanic_dataset.csv')
#把标签和特征分开
y_train1=features['Survived']
X_train=features.drop('Survived',axis=1)

X_train.info()

X_train.isnull().sum()

X_train1=X_train.copy()
X_train1['Age'].replace(np.nan,np.nanmedian(X_train1['Age']),inplace=True)

age_sex_mdeian=X_train.groupby('Sex').Age.median()
X_train2=X_train.set_index('Sex')
X_train2.Age.fillna(age_sex_mdeian,inplace=True)
X_train2.reset_index(inplace=True)
Xage2=X_train2['Age']

age_Pclass=X_train.groupby(['Pclass','Sex']).Age.median()
X_train.set_index(['Pclass','Sex'],inplace=True)
X_train.Age.fillna(age_Pclass,inplace=True)
X_train.reset_index(inplace=True)

meanage=[[],[],[]]
#性别仓位中位数
meanage[0]=X_train.Age.mean()
#中位数
meanage[1]=X_train1.Age.mean()
#性别中位数
meanage[2]=X_train2.Age.mean()

plt.rcParams['font.family']=['SimHei']
fig1=plt.figure()
ax=fig1.add_subplot(2,2,1)
plt.title('原数据集')

sns.distplot(X_train['Age'].dropna(),hist=True,kde=True,axlabel=None)
ax=fig1.add_subplot(2,2,2)
plt.title('2数据集')
sns.distplot(X_train1['Age'].dropna(),hist=True,kde=True,axlabel=None)
ax=fig1.add_subplot(2,2,3)
plt.title('3数据集')
sns.distplot(X_train2['Age'].dropna(),hist=True,kde=True,axlabel=None)
plt.show()