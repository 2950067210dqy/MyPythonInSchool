import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris #导入数据集
def partOne():
    plt.rcParams['font.family'] = ['SimHei']  # 用于画图时显示中文
    # 1.使用sklearn 获得iris数据集
    irisBunch = load_iris()
    # 2.查看iris数据集把取出DATA数据
    irisData = irisBunch.data
    # 3.合并DATA和target的数据,并加列名
    irisFeature = irisBunch.feature_names
    irisClass = irisBunch.target
    irisClassName = irisBunch.target_names
    # (1)用pandas
    colums = ['花萼-length', '花萼-width', '花瓣-length', '花瓣-width']
    irisDataPD = pd.DataFrame(irisData, columns=colums)
    irisDataPD['花的类别-class'] = irisClass
    # (2)用numpy(加列名必须要用到pandas)
    irisClassNP = irisClass.reshape(len(irisClass), 1)
    irisDataNP = np.concatenate((irisData, irisClassNP), axis=1)


    return [irisDataNP,irisDataPD,colums,irisClassNP,irisClassName]

def partTwo(data=[]):
    irisDataNP=data[0]
    irisDataPD=data[1]
    colums=data[2]
    irisClassNP=data[3]
    irisClassName=data[4]
    # 5.画出相关性矩阵np.corrcoef(data, rowvar=False)，打印出与最能影响class的2个特征
    corr = np.corrcoef(irisDataNP, rowvar=False)
    # 6.先把class相关的那一列（最后一列）
    corrClass = corr[:, -1]
    # 7.相关一列绝对值，然后排序
    corrCLassABS = np.abs(corrClass)
    corrCLassDF = pd.DataFrame(corrCLassABS)
    corrCLassDFSort = corrCLassDF.sort_values(by=0)
    corrClassDFIndex = corrCLassDFSort.index
    corrClassDFIndexArray = np.array(corrClassDFIndex)

    corrClassDFIndexArraySub = corrClassDFIndexArray[-3:-1]
    corrClassDFIndexArrayZero = list(np.zeros(len(corrClassDFIndexArraySub)))
    for i in range(len(corrClassDFIndexArraySub)):
        corrClassDFIndexArrayZero[i] = colums[corrClassDFIndexArraySub[i]]

    return [corrClassDFIndexArraySub,colums,irisDataPD,corrClassDFIndexArrayZero, irisClassNP,irisClassName]

def partThree(data=[]):
    corrClassDFIndexArraySub=data[0]
    colums=data[1]
    irisDataPD=data[2]
    corrClassDFIndexArrayZero=data[3]
    irisClassNP=data[4]
    irisClassName=data[5]
    # 画图
    fig = plt.figure(figsize=(10, 7))
    # title
    color = ['red', 'blue', 'green']
    for i in range(len(corrClassDFIndexArraySub)):
        ax = fig.add_subplot(2, 2, i + 1)
        plt.xlabel(colums[corrClassDFIndexArraySub[i]])
        plt.ylabel('花的类别-class')
        for j in range(len(color)):
            ax.scatter(irisDataPD[corrClassDFIndexArrayZero[i]][j * 50:(j + 1) * 50], irisClassNP[j * 50:(j + 1) * 50],
                       c=color[j], label=irisClassName[j])
        plt.legend()
    fig.suptitle('iris相关', fontsize=20)
    plt.show()

partThree(partTwo(partOne()))


