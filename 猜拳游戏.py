#猜拳游戏
#邓亲优20
import random
import re
dic={0:"剪刀",1:"石头",2:"布"}
def switch(key):
    return dic.get(key)
print("-"*32)
print(" "*(32//2-4)+"猜拳游戏")
isContinue='y'
while isContinue=='y' or isContinue=='Y':
    ytemp = input("请输入（0剪刀，1石头，2布）：")
    while not re.match(r'^[012]*$', ytemp):
        ytemp = input(f"{ytemp}值非法，请重新输入（0剪刀，1石头，2布）")
    ytemp=int(ytemp)
    mtemp=random.randint(0,2)
    print(f"你出拳的是   {switch(ytemp)}")
    print(f"电脑出拳是   {switch(mtemp)}")
    if(mtemp==ytemp):
        print("平手！")
    elif mtemp == 0 and ytemp == 1:
        print("恭喜您，您赢了！")
    elif mtemp == 0 and ytemp == 2:
        print("您输了，再接再厉！")
    elif mtemp == 1 and ytemp == 0:
        print("您输了，再接再厉！")
    elif mtemp == 1 and ytemp == 2:
        print("恭喜您，您赢了！")
    elif mtemp == 2 and ytemp == 0:
        print("恭喜您，您赢了！")
    elif mtemp == 2 and ytemp == 1:
        print("您输了，再接再厉！")
    isContinue=input("是否继续猜拳? y/n")

print(" "*(32//2-4)+"猜拳结束")
print("-"*32)
