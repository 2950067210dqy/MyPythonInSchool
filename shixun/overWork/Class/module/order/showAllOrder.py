from shixun.overWork.Class.module.order.selectOrder import selectOrder
from shixun.overWork.Class.module.order.deleteOrder import deleteOrder
import re
def showAllOrder(loginUser=None):
    print("*" * 30 + "欢迎来到九江学院外卖平台----订单界面" + "*" * 30)
    print("查询中....")
    print("查询成功!")
    selectOrder(loginUser=loginUser)
    print("订单操作： 1.删除订单       2.返回上一级")
    order = input("请输入你的指令:")
    while not re.match(r'[1-2]', order) or len(order) == 0 or len(order)>1:
        order = input(f"{order}值格式错误，请重新输入你的指令:")
    if order == "1":
        deleteOrder(loginUser=loginUser)
    if order == "2":
        return False
    isAgain = input("是否继续操作订单?y/n")
    while not re.match(r'^[yYnN]*$', isAgain) or len(isAgain) == 0 or len(isAgain)>1:
        isAgain = input(f"{isAgain}值非法，是否继续操作订单?y/n")
    if isAgain == "y" or isAgain == "Y":
        return True
    else:
        return False

    pass