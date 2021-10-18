import re
from shixun.overWork.Class.IO.AllUserIO import AllUserIO
from shixun.overWork.Class.module.regist import register
from shixun.overWork.Class.pojo.User import User
from shixun.overWork.Class.pojo.SuperUser import SuperUser
from shixun.overWork.Class.pojo.Merchanter import Merchanter
def login():
    perssmionsTxt = {1: "用户登录", 2: "商家登录", 3: "管理员登录"}
    print("*" * 30 + "登录模块" + "*" * 30)
    print("1.用户登录" + " " * 10 + "2.商家登录" + " " * 10 + "3.管理员登录")
    permissons = input("请输入你要选择的登录角色:")
    while not re.match(r'^[1-3]*$', permissons)  or len(permissons)==0 or len(permissons)>1:
        permissons = input(f"{permissons}值非法，请重新输入你要选择的登录角色:")
    print(f"{'*' * 6}欢迎进入{perssmionsTxt[int(permissons)]}{'*' * 6}")
    usernameInput = input("请输入您的账号[账号都为数字]，‘/’键找回密码,‘.’键注册账号:")
    while not re.match(r'^[0-9/.]*$',usernameInput)  or len(usernameInput)==0 :
        usernameInput = input(f"{usernameInput}值非法，请重新输入您的账号[账号都为数字]，‘/’键找回密码,‘.’键注册账号:")
    if usernameInput=="/":
        isFoundPasswordAgain = isFoundPassword()
        while isFoundPasswordAgain:
            isFoundPasswordAgain = isFoundPassword()
        return False
    if usernameInput==".":
        # 注册
        registerAgain = register()
        while registerAgain:
            registerAgain = register()
    passwordInput = input("请输入您的密码，‘/’键找回密码,‘.’键注册账号 :")
    if passwordInput=="/":
        isFoundPasswordAgain=isFoundPassword()
        while isFoundPasswordAgain:
            isFoundPasswordAgain = isFoundPassword()
        return False
    if usernameInput==".":
        # 注册
        registerAgain = register()
        while registerAgain:
            registerAgain = register()
    user = None
    userdic = None
    if int(permissons)==1:
        user = User(username=usernameInput, password=passwordInput)
        userdic = user.__dict__  # 将对象转换为字典
    if int(permissons)==2:
        user = Merchanter(username=usernameInput, password=passwordInput)
        userdic = user.__dict__  # 将对象转换为字典
    if int(permissons)==3:
        user = SuperUser(username=usernameInput, password=passwordInput)
        userdic = user.__dict__  # 将对象转换为字典
    io = AllUserIO(userdic)
    loginUser=None
    loginUser=io.login()
    if loginUser:
       print("登录成功")
       return loginUser
    else:
        # 登录失败
        print("登录失败，账号密码错误！")
        print("-" * 10 + "正在重新跳转到登录模块" + "-" * 10)
        return False
def isFoundPassword():
    print("."*6+"欢迎来到找回密码模块"+"."*6)
    usernameFoundInput=input("请输入您的要找回密码的账号[账号都为数字]，“q/Q”键退出:")
    while not re.match(r'^[0-9qQ/]*$',usernameFoundInput)  or len(usernameFoundInput)==0:
        usernameFoundInput = input(f"{usernameFoundInput}值非法，您的要找回密码的账号[账号都为数字]，‘q/Q’键 退出:")
    if usernameFoundInput=="q" or usernameFoundInput =="Q":
        print("." * 6 + "找回密码模块已经退出" + "." * 6)
        return
    user=User(username=usernameFoundInput)
    userdic=user.__dict__
    io=AllUserIO(user=userdic)
    if io.judgeRepeat():
        password=input("请输入您要修改的密码:")
        rePassword=input("请再次输入您要修改的密码")
        while password!=rePassword:
            print("两次密码不一样！")
            password = input("请重新输入您要修改的密码:")
            rePassword = input("请再次输入您要修改的密码")
        user=User(username=usernameFoundInput,password=password)
        userdic=user.__dict__
        io.user=userdic
        io.updatePasswordByUsername()
        print("修改成功！")
        print("-" * 10 + "正在跳转到登录模块" + "-" * 10)
        return False
    else:
        print("未找到该用户")
        isAgain = input("是否继续找回密码?y/n")
        while not re.match(r'^[yYnN]*$', isAgain)  or len(isAgain)==0 or len(isAgain)>1:
            isAgain = input(f"{isAgain}值非法，是否是否继续找回密码?y/n")
        if isAgain == "y" or isAgain == "Y":
            return True
        else:
            print("-" * 10 + "正在跳转到登录模块" + "-" * 10)
            print("-" * 10 + "跳转成功" + "-" * 10)
            return False
    pass

