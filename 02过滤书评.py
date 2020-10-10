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
