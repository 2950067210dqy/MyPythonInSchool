#猜数字游戏
#邓亲优20
import random
import re
oldWords=[]
# 得到四位且每位跟其他位不重复的数字 且不能是之前生成的数字
def getFourRandomWord():
    word="1"
    for i in range(3):
        varb=str(random.randint(1, 9))
        while varb  in word:
            varb = str(random.randint(0, 9))
        else:
            word=word+varb

    while word  in oldWords:
        word = "1"
        for i in range(3):
            varb = str(random.randint(1, 9))
            while varb in word:
                varb = str(random.randint(0, 9))
            else:
                word = word + varb
    oldWords.append(word)
    return word
# 检测用户输入的4位数字每位是否跟其他位重复
def inputRepeat(words):
    for i in range(len(words)):
        for j in range(i+1,len(words)):
            if words[i] == words[j]:
                return True
    return False
    pass


print("欢迎来到猜数字游戏！")
print("规则为：系统随机生成一个4位数(1000-9999)数里的每一位跟其他位都不重复，然后猜这个数字！")
print("------猜数字游戏开始-----")
print("系统正在生成随机的4位且每位都与其他位不相同的数字...")
mword = getFourRandomWord()
print("生成成功...")
isContinue = ""
while True:
    if isContinue == 'y' or isContinue == 'Y':
        isContinue = ""
        print("----新一轮游戏开始----")
        print("系统正在生成随机的4位且每位都与其他位不相同的数字...")
        mword = getFourRandomWord()
        print("生成成功...")
    # print(f"系统的随机数字为{mword}")
    # print(f"已经生成过的随机数{oldWords}")
    yword = input("请输入您所猜数字(输入必须为4位每一位都与其他位不重复的数字)：")
    while not re.match(r'^[0-9]*$', yword) or len(yword) != 4 or inputRepeat(yword):
        yword = input("您输入的数字不符合要求(输入必须为4位每一位都与其他位不重复的数字)，请重新输入：")
    num = 0
    location = 0
    if mword == yword:
        print(f"恭喜您猜对了！数字为{mword}")
        isContinue = input("是否继续猜数字游戏？Y/N")
        if isContinue != 'y' and isContinue != 'Y':
            break
    else:
        for i in range(len(mword)):
            if mword[i] in yword:
                num = num + 1
            if mword[i] == yword[i]:
                location = location + 1
        print("您猜的不正确！")
        print(f"您猜的数字值正确的个数为{num},数字位置的正确个数为{location}")

print("-----猜数字游戏结束-----")
