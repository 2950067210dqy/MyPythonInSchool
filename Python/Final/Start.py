# 开发工具：PyCharm
import re  # 导入正则表达式模块
import os  # 导入操作系统模块


from Final.adminView import adminView
from Final.userView import UserView

userFile = "userList.txt"
adminFile="admin"

def menu():

    print('''

    │   =============== 功能菜单 ===============   │
    │                                             │
    │   1 注册                                     
    │   2 用户登录                                 │ 
    │   3 管理员登录                               │
    │   0 退出系统                                 │
    │  ========================================== │
   
    ''')
def main():
    global start
      # 标记是否退出系统
    start = True
    while (start):
        menu()  # 显示菜单
        option=choose()
        if option == 0:  # 退出系统
            print('您已退出快递查询系统！')
            start = False
        elif option == 1:
            register()
        elif option == 2:
            userLogin()
        elif option == 3:
            adminLogin()

def choose():
    data = input("请选择：")
    try:
        inputData = eval(data)
        if type(inputData) == int:
            # break
            if inputData in range(0, 4):
                return inputData
    except:
        pass

def register():
    print("---用户注册---")
    i=1
    userList = []
    isCoutinue = True
    while isCoutinue:
        try:
            username = input("请输入用户名：")
            password = input("请输入密码：")
        except:
            print("输入存在错误，重新录入信息")
            continue
        with open('num.txt', 'r') as a:
            num = int(a.read())
            numm = num + 1
            print(type(num))
        f = open('num.txt', 'w+')
        strnum = str(numm)
        f.write(strnum)
        f.close()

        user = {"id": numm, "username": username, "password": password,'expNum':0}
        userList.append(user)
        isCoutinue=False
    save(userList)
    print("注册成功！！！")
def save(userList):
    try:
        user_txt = open(userFile, "a")
    except Exception as e:
        user_txt = open(userFile, "w")
    for info in userList:
        user_txt.write(str(info) + "\n")
    user_txt.close()  # 关闭文件

def userLogin():
    global start
    print("---用户登录---")
    mark = True
    while mark:
            print("请输入你的账号与密码")
            username = input("请输入用户名：")
            password = input("请输入密码：")
            if not username or not password:
                        break
            with open(userFile, 'r') as file:
                userlist = file.readlines()
                print(userlist)
                for list in userlist:
                    d = dict(eval(list))
                    print()
                    if d['username'] == username:
                        if d['password'] == password:
                            print("登录成功")
                            mark = False
                            UserView(d['id'],d['username'],d['password'])
                        else:
                            print("密码错误,请重新输入")
                            mark = True

def adminLogin():
    print("---管理员登录---")
    mark = True
    while mark:
        if os.path.exists(adminFile):
            print("请输入管理员账号与密码")
            username = input("请输入用户名：")
            password = input("请输入密码：")
            if not username or not password:
                break
            with open(adminFile, 'r') as file:
                adminlist = file.readlines()
                for list in adminlist:
                    d = dict(eval(list))
                    if d['username'] == username:
                        if d['password'] == password:
                            print("登录成功")
                            adminView()
                            mark = False
                            start = False
                        else:
                            print("密码错误,请重新输入")

if __name__ == "__main__":
    main()
