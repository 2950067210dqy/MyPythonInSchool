import random
import re
#scores=[random.randint(90,100) for i in range(random.randint(3,10))]
pingwei = random.randint(3,10)
print(f"随机生成的评委有{pingwei}名，")
scores=[]
for i in range(pingwei):
    score = input(f"第{i + 1}位评委开始打分(0-100分)：")
    while not re.match(r'[0123456789]', score) or len(score) == 0 or len(score) > 3 or int(score) > 100:
        score = input(f"{score}值格式错误，请重新输入分数(0-100分):")
    print(f"第{i+1}位评委打分{score}分")
    scores.append(int(score))
print(f"去掉一个最高分:{max(scores)}分\n去掉一个最低分:{min(scores)}分")
del scores[scores.index(max(scores))]
del scores[scores.index(min(scores))]
print(f"平均分为:{sum(scores)/len(scores)}")
