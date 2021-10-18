import re
usernameInput=input("请输入一个三位以上的整数：")
while not re.match(r'^[0-9]*$', usernameInput)  or len(usernameInput)<4:
    usernameInput = input(f"{usernameInput}值非法，请重新输入一个三位以上的整数：")
usernameInput=usernameInput[0:len(usernameInput)-2:1]
print(f"百位及以上的数字为:{usernameInput}")