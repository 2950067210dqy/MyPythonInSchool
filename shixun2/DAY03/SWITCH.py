import re
def switch(i):
    if int(i)<1 or int(i)>7:
        return "值错误！"
    return f"星期{i}"
t=input("请输入1-7:")
while not re.match(r'^[1-7.]*$',t):
    t = input(f"{t}值非法，请重新输入")
print(switch(t))
