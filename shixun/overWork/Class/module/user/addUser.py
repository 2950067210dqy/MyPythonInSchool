import re
from shixun.overWork.Class.pojo.User import User
from shixun.overWork.Class.IO.AllUserIO import AllUserIO
def addUser(loginUser=None):
    print("*" * 10 + "用户添加模块" + "*" * 10)

    usernameInput = input("请输入账号[都为数字]:")
    while not re.match(r'^[0-9]*$', usernameInput) or len(usernameInput) == 0:
        usernameInput = input(f"{usernameInput}值非法，请重新输入账号[账号都为数字]")
    password = input("请输入密码:")
    rePassword = input("请再次输入密码")
    while password != rePassword:
        print("两次密码不一样！")
        password = input("请重新输入密码:")
        rePassword = input("请再次输入密码")
    print("-" * 5 + "添加中，请稍后" + "-" * 5)
    user = User(username=usernameInput, password=password)
    userdic = user.__dict__  # 将对象转换为字典
    io = AllUserIO(userdic)
    if io.setByRegist():
        # 注册成功
        print(f"添加成功，您的添加的用户账号为{usernameInput}，密码为{password}!!!")
    else:
        # 注册失败
        print("账号名已被添加，请更换 ！")
        print("添加失败")
