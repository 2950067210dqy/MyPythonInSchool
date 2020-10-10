#邓亲优20
import random
print("欢迎来到猜字游戏！")
print("------猜字游戏开始-----")
yword=int(input("请输入您所猜数字(1-10之间但不包括10)"))
while yword<1 or yword >=10:
    yword = int(input("您输入的数字不符合要求，请重新输入(1-10之间但不包括10)"))
mword=random.randint(1,9)
print("系统的数字为%d"%mword)
x=0
while True:
    x+=1
    if yword>mword:
        yword=int(input("您输入的数字太大，请重新输入(1-10之间但不包括10)"))
        while yword < 1 or yword >= 10:
            yword = int(input("您输入的数字不符合要求，请重新输入(1-10之间但不包括10)"))
    elif yword<mword:
        yword =int(input("您输入的数字太小，请重新输入(1-10之间但不包括10)"))
        while yword < 1 or yword >= 10:
            yword = int(input("您输入的数字不符合要求，请重新输入(1-10之间但不包括10)"))
    else:
        if x<=2:
            print("您太棒了！")
            break
        elif 2<x<=4:
            print("恭喜你猜对了！")
            break
        elif 4<x<=6:
            print("终于猜出来了！")
            break
        elif x>6:
            print("你太笨了，游戏结束!")
            break
print("-----猜字游戏结束-----")

