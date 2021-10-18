import random
import re
def delval(list,max,min):
    temp=0
    for i in list:
        for j in i.values():
                if j == max :
                    print(f"去掉第{temp+1}位评委打的最高分{j}分")
                    list.pop(temp)
                    break
                elif j == min:
                    print(f"去掉第{temp + 1}位评委打的最低分{j}分")
                    list.pop(temp)
                    break

        temp+=1
    return list
def Max(list):
    templist=[]
    for i in list:
        for j in i.values():
            templist.append(j)
    return max(templist)
def Min(list):
    templist = []
    for i in list:
        for j in i.values():
            templist.append(j)
    return min(templist)
def Average(list):
    templist = []
    for i in list:
        for j in i.values():
            templist.append(j)
    return sum(templist)/len(templist)
    pass
pingwei = random.randint(2,5)
print(f"随机生成的评委有{pingwei}名，")
scroes=[]
for i in range(pingwei):
    score = input(f"第{i+1}位评委开始打分(0-100分)：")
    while not re.match(r'[0-100]',score)   or len(score)==0 or len(score)>3 or int(score)>100:
        score =input(f"{score}值格式错误，请重新输入分数:")
    scroes.append({i:int(score)})
maxval=Max(scroes)
minval=Min(scroes)
newscroes=delval(scroes,maxval,minval)
print(f"平均分为{Average(newscroes)}")


