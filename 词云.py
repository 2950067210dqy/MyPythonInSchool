import re
import jieba
import collections
import numpy as np
import wordcloud

from PIL import Image
import matplotlib.pyplot  as plt
import collections #导入collection库
import jieba
# 获取书评

with open('bookComments.txt', 'r') as fp:  # 打开文件
    bookComments=fp.read() # 将文件内容读取到bookcomments中

r='[。，,！.?&!;？*；、  （）( )《》]+|[a-zA-Z]+|[0-9]'
Comments_data = re.sub(r,'',bookComments) # 将符合模式的字符去除
print(Comments_data)
Comments=Comments_data.split('\n')#产生了列表Comments
print("一共有{}条书评:".format(len(Comments)))
print('一共有%d条书评:'%(len(Comments)))

CommentsTuple=tuple(Comments)
#Comments[0]='修改第一条书评'
#print(Comments)
#CommentsTuple[0]='修改第一条书评'
#print(CommentsTuple)
with open('bookCommentsNew.txt', 'w') as fp:
    for item in CommentsTuple:
        fp.write(item+'\n')




# 过滤书评

#打开书评文件并将文件内容读取到bookcomments当中
with open('bookCommentsNew.txt', 'r') as fp:
    bookComments=fp.read()
#把每一行的书评转换为列表
Comments=bookComments.split('\n')
#将列表转换为元组
CommentsTuple=tuple(Comments)
#构建过滤规则
rule = lambda x:len(set(x))/len(x)>0.6



#产生了过滤之后的书评
result = filter(rule,CommentsTuple)


#显示原始书评
print('********原始书评***************')
for comment in CommentsTuple:
    print(comment)
print(len(CommentsTuple))


#显示过滤之后的书评
print('********过滤后的书评见bookCommentsNew1.txt文件***********')
i=0
with open('bookCommentsNew1.txt','w') as fp:
    for item in result:
        fp.write(item+'\n')
        i=i+1
print(i)



#词频统计

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


# 生成词云


with open('bookCommentsNew1.txt', 'r') as fp:
    bookComments=fp.read()
Comments_list_exact = jieba.cut(bookComments,cut_all =False) # 精确模式分词
d=dict()
for key in Comments_list_exact:
    d[key] = d.get(key, 0) + 1
#print(d)
#词频展示
mask1 = np.array(Image.open('bj.jpg')) # 定义词频背景
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