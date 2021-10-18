from shixun.overWork.Class.module.food.selectFood import selefctFood
from shixun.overWork.Class.module.food.deleteFood import deleteFood
from shixun.overWork.Class.module.food.updateFood import updateFood
from shixun.overWork.Class.module.food.addFood import addFood
import re
def showAllFood(loginUser=None):
    print("*" * 30 + "欢迎来到九江学院外卖平台----商品界面" + "*" * 30)
    print("查询中....")
    print("查询成功!")
    selefctFood(loginUser=loginUser)
    print("订单操作： 1.删除商品        2.更新商品          3.返回上一级")
    order = input("请输入你的指令:")
    while not re.match(r'[1-3]', order) or len(order) == 0 or len(order)>1:
        order = input(f"{order}值格式错误，请重新输入你的指令:")
    if order == "1":
        deleteFood(loginUser=loginUser)
    if order == "2":
        updateFood(loginUser=loginUser)
    if order == "3":
        return False
    isAgain = input("是否继续操作商品?y/n")
    while not re.match(r'^[yYnN]*$', isAgain) or len(isAgain) == 0 or len(isAgain)>1:
        isAgain = input(f"{isAgain}值非法，是否继续操作商品?y/n")
    if isAgain == "y" or isAgain == "Y":
        return True
    else:
        return False

    pass