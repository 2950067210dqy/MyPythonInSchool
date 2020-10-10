# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 14:05:52 2019

@author: Administrator
"""

import re
import jieba
import collections
import numpy as np
import wordcloud

from PIL import Image
import matplotlib.pyplot  as plt
import collections #导入collection库
import jieba
with open('bookCommentsNew1.txt', 'r') as fp:
    bookComments=fp.read()
Comments_list_exact = jieba.cut(bookComments,cut_all =False) # 精确模式分词
d=dict()
for key in Comments_list_exact:
    d[key] = d.get(key, 0) + 1
#print(d)
#词频展示
mask1 = np.array(Image.open('bg.png')) # 定义词频背景
wc = wordcloud.WordCloud(
    font_path='C:/Windows/Fonts/simhei.ttf', # 设置字体格式
    width=500, height=400,
    mask=mask1, # 设置背景图
    max_words=200, # 最多显示词数
    max_font_size=100, # 字体最大值
    background_color='white', 
    font_step=3,
    random_state=True,
    prefer_horizontal=0.9)
wc.generate_from_frequencies(d) # 从字典生成词云
image_colors = wordcloud.ImageColorGenerator(mask1) # 从背景图建立颜色方案
wc.recolor(color_func=image_colors) # 将词云颜色设置为背景图方案
plt.imshow(wc) # 显示词云
plt.axis('off') # 关闭坐标轴
plt.show() # 显示图像
