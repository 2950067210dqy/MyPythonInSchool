from shixun.overWork.Class.module.user.selectUser import selectUser
from shixun.overWork.Class.module.user.addUser import addUser
from shixun.overWork.Class.module.user.deleteUser import deleteUser
from shixun.overWork.Class.module.user.updateUser import updateUser
import re
def showAllUser(loginUser=None):
    print("*" * 30 + "欢迎来到九江学院外卖平台----用户信息界面" + "*" * 30)
    print("查询中....")
    print("查询成功!")
    selectUser(loginUser=loginUser)
    print("用户操作： 1.删除用户       2.增加用户        3.编辑用户         4.返回上一级")
    order = input("请输入你的指令:")
    while not re.match(r'[1-4]', order) or len(order) == 0 or len(order)>1:
        order = input(f"{order}值格式错误，请重新输入你的指令:")
    if order == "1":
       deleteUser(loginUser=loginUser)
    if order == "2":
        addUser(loginUser=loginUser)
    if order == "3":
        updateUser(loginUser=loginUser)
    if order == "4":
        return False
    isAgain = input("是否继续操作用户信息?y/n")
    while not re.match(r'^[yYnN]*$', isAgain) or len(isAgain) == 0 or len(order)>1:
        isAgain = input(f"{isAgain}值非法，是否继续操作用户信息?y/n")
    if isAgain == "y" or isAgain == "Y":
        return True
    else:
        return False

    pass