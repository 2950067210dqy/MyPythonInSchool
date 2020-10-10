import re
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
