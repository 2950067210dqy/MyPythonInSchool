import re
from shixun.overWork.Class.pojo.User import User
from shixun.overWork.Class.pojo.SuperUser import SuperUser
from shixun.overWork.Class.pojo.Merchanter import Merchanter

from shixun.overWork.Class.IO.AllUserIO import AllUserIO
def register():
    permissionsTXT={"1":"用户","2":"商家"}
    print("*" * 30 + "注册模块" + "*" * 30)
    usernameInput=input("请输入您的账号[都为数字]:")
    while not re.match(r'^[0-9]*$', usernameInput)  or len(usernameInput)==0:
        usernameInput = input(f"{usernameInput}值非法，请重新输入您的账号[账号都为数字]")
    passwordInput=input("请输入您的密码:")
    permissionsInput=input("请输入您要注册的账号类型,1为用户，2为商家：")
    while not re.match(r'^[1-2]*$', permissionsInput)  or len(permissionsInput)==0 or len(permissionsInput)>1:
        permissionsInput = input(f"{permissionsInput}值非法，请重新输入您要注册的账号类型,1为用户，2为商家：")
    print("-"*5+"注册中，请稍后"+"-"*5)
    user=None
    userdic=None
    if int(permissionsInput)==1:#普通用户
        user=User(username=usernameInput,password=passwordInput)
        userdic=user.__dict__#将对象转换为字典
        pass
    else:#商家
        user = Merchanter(username=usernameInput,password= passwordInput)
        userdic=user.__dict__
        pass
    io = AllUserIO(userdic)
    if io.setByRegist():
        # 注册成功
        print(f"恭喜您注册成功，您的注册账号为{usernameInput}，密码为{passwordInput}，账号类型为{permissionsTXT[permissionsInput]}!!!")
    else:
        # 注册失败
        print("账号已被注册，请更换 ！")
        print("注册失败")

    isAgain = input("是否继续注册?y/n")
    while not re.match(r'^[yYnN]*$', isAgain)  or len(isAgain)==0:
        isAgain = input(f"{isAgain}值非法，是否重新注册?y/n")
    if isAgain == "y" or isAgain == "Y":
        return True
    else:
        print("-"*10+"正在跳转到登录模块"+"-"*10)
        print("-" * 10 + "跳转成功" + "-" * 10)
        return False

