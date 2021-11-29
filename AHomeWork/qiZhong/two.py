
word=input("请输入一个单词:")
firstletter=""
secondletter=""
temp=True
for i in range(0,len(word)-1):
    firstletter=word[i]
    secondletter=word[i+1]
    if firstletter>secondletter:
        temp=False
        break
if temp:
    print("该单词是按照字典序排列")
else:
    print("该单词不是按照字典序排列")