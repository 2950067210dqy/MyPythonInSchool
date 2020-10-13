#新增功能：将导入的单词存储在文本当中


import os
import random
#添加单词功能
def ImportWords(WordsFile,word):
    WordsFile.write(word+"\n")
    WordsFile.flush()
#单词乱序功能
def LuanXu(word):
    Lword=""
    while word:  # word 不是空串循环
        # 根据 word 长度产生 word 的随机位置
        position = random.randrange(len(word))
        # 将 position 位置的字母组合到乱序后单词
        Lword += word[position]
        # 通过切片将 position 位置的字母从原单词中删除
        word = word[:position] + word[(position + 1):]
    return Lword
# 查询所有单词
def ChaXunAllWords(WordsFile,option=1):
    WordsFile.seek(os.SEEK_SET);
    list = WordsFile.readlines()
    list=StrSplitOfList(oldList=list,string="\n")
    if option==1:
        print("-" * 10 + "查询成功" + "-" * 10)
        print("当前字库的单词为："+ str(list))
    return list
# 查询要插入的单词是否在词库里重复
def ChaXunSingleWord(word,wordList):
    for i in wordList:
        if word == i:
            return True
    else:
        return False
#  将列表中的字符串切片
def StrSplitOfList(oldList,string):
    newList=[]
    for i in oldList:
        newList.append(str(i).split(string)[0])
    return newList
WordsFile=open("Words.txt","a+")
#创建单词序列
WORD=input("当前字库有"+str(len(ChaXunAllWords(WordsFile=WordsFile,option=0)))+"个单词,‘C’键查询当前所有单词，是否添加字库? （Y/N）:\n")
while WORD=="Y" or WORD=="y" or WORD=="C" or WORD=="c":
    if WORD=="C" or WORD=="c":
        ChaXunAllWords(WordsFile=WordsFile)
    else:
        WORD=input("请输入要添加的单词\n")
        # 添加的单词重复
        if ChaXunSingleWord(WORD,ChaXunAllWords(WordsFile=WordsFile,option=0)):
            print("您添加的单词存储在词库中哦！\n")
        else:
            ImportWords(WordsFile,WORD)
        print("当前字库有" + str(len(ChaXunAllWords(WordsFile=WordsFile,option=0))) + "个单词")
    WORD=input("‘C’键查询当前所有单词，是否继续添加字库?（Y/N）:\n")
else:
    print("-----------单词导入操作完成，开始猜单词--------")
    WORDS = tuple(ChaXunAllWords(WordsFile=WordsFile, option=0))
    WordsFile.close()

print(WORDS)

#开始游戏
print("""欢迎参加猜单词游戏
把字母组合成一个正确的单词.""")
iscontinue="y"
while iscontinue=="y" or iscontinue=="Y":
    #从序列中随机挑出一个单词
    word=random.choice(WORDS)
    #一个用于判断玩家是否猜对的变量
    correct=word
    #创建乱序后单词
    jumble=LuanXu(word)
    print("乱序后单词:",jumble)
    guess=input("请你猜:")
    if guess==correct:
        print ("真棒，你猜对了！")
    while guess!=correct and guess!="":
        # 跳过该单词
        if guess=="c" or guess=="C":
            break
        else:
            print("对不起不正确.")
            guess=input("继续猜('c'键跳过该单词):")
    iscontinue=input("\n是否继续猜单词（Y/N）:")

