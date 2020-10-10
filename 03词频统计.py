# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 13:21:54 2019

@author: Administrator
"""
#import re
import jieba

#打开文件
with open('bookCommentsNew1.txt', 'r') as fp:
    bookComments=fp.read()

#开始分词
Comments_list_exact = jieba.lcut ( bookComments, cut_all =False)
# 精确模式分词

print(Comments_list_exact)

#创建字典
d = dict()
for key in Comments_list_exact:
    d[key] = d.get(key, 0) + 1

print(d)
#print(d['很'])
#print(d['很快'])

