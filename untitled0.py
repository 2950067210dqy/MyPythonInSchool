# -*- coding: utf-8 -*-
"""
Created on Sat Sep 18 08:11:17 2021

@author: 优哥
"""

import numpy as np
'''
size=(5,5)]


arr1=np.random.randint(200,size=size)
arr2=np.random.randint(200,size=size)
print(f"arr1:\n{arr1}")
print(f"arr2:\n{arr2}")
arr3=np.hstack((arr1,arr2))
print(f"横向合并为:\n{arr3}")
arr4=np.vstack((arr1,arr2))
print(f"纵向合并为:\n{arr4}")
arr5=arr4.flatten()
print(f"数据扁平化:\n{arr5}")



size=(50,15)
arr6=np.random.randint(1,1001,size)
print(f"arr6:\n{arr6}")
print(f"数组的和:\n{np.sum(arr6)}")
print(f"数组纵轴的和:\n{np.sum(arr6,axis=0)}")
print(f"数组横轴的和:\n{np.sum(arr6,axis=1)}")
print(f"数组的均值:\n{np.mean(arr6)}")
print(f"数组纵轴的均值:\n{np.mean(arr6,axis=0)}")
print(f"数组横轴的均值:\n{np.mean(arr6,axis=1)}")
print(f"数组的标准差:\n{np.std(arr6)}")
print(f"数组纵轴的标准差:\n{np.std(arr6,axis=0)}")
print(f"数组横轴的标准差:\n{np.std(arr6,axis=1)}")
'''
import pandas as pd
from sklearn.datasets import load_iris #导入数据集iris  
iris = load_iris() #载入数据集
arr4=np.hstack((iris.data,iris.target.reshape(150,1)))
df1=pd.DataFrame(arr4,columns=['花萼-length', '花萼-width', '花瓣-length', '花瓣-width',"花名-name"])
