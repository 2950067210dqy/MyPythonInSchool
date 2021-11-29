import numpy as np
import  pandas as pd
import  matplotlib.pyplot as plt
from sklearn.datasets import load_boston
d=load_boston()

feature=d.data
price=d.target
data=pd.DataFrame(d.data,columns=d.feature_names)
price=price.reshape(506,1)
data1=np.concatenate((feature,price),axis=1)#第一种合并方法
#data['price']=d.target#第二种合并方法  如果是dataframe格式
name=d.feature_names
names=list(np.zeros(len(name)))
#for循环在手机照片里

#第二种方法
data2=pd.DataFrame(d.data)
data2.columns=names
data2['房价']=d.target




corr=np.corrcoef(data,rowvar=False)#相关性
pcorr=corr[:,-1]#房价相关性
pcorr=np.abs(pcorr)#取绝对值
pcorr=pd.DataFrame(pcorr)#为了排序后索引也会变 转成dataframe
pcorr1=pcorr.sort_values(by=0)
b=pcorr1.index
b=np.array(b)
b1=b[-5:-1]
b2=np.zeros(len(b1))
b2=list(b2)
for i  in range(len(b1)):
    b2[i]=names[b1[i]]



#
# fig=plt.figure(figsize=(10,7))
# ax1=fig.add_subplot(2,2,1)
# plt.ylabel("price")
# ax1.scatter(feature[:,2],price,label=names[2])
# plt.legend()
#
# ax2=fig.add_subplot(2,2,1)
# plt.ylabel("price")
# ax2.scatter(feature[:,10],price,label=names[10])
# plt.legend()
#
# ax3=fig.add_subplot(2,2,1)
# plt.ylabel("price")
# ax3.scatter(feature[:,5],price,label=names[5])
# plt.legend()
#
# ax4=fig.add_subplot(2,2,1)
# plt.ylabel("price")
# ax4.scatter(feature[:,12],price,label=names[12])
# plt.legend()
#
# plt.show()

fig=plt.figure(figsize=(10,7))
for i in range(len(b1)):
    ax=fig.add