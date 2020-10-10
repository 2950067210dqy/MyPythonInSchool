#邓亲优20
import random
print("-"*32)
print(" "*(32//2-4)+"猜拳游戏")
ytemp=int(input("请输入（0剪刀，1石头，2布）："))
mtemp=random.randint(0,2)
print(f"电脑出拳是{mtemp}")
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
print(" "*(32//2-4)+"猜拳结束")
print("-"*32)