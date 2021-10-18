import re
from shixun.overWork.Class.module.user.showAllUser import showAllUser
from shixun.overWork.Class.module.merchanter.showAllMerchanter import showAllMerchanter
from shixun.overWork.Class.module.food.showAllFood import showAllFood
from shixun.overWork.Class.module.order.showAllOrder import showAllOrder
from shixun.overWork.Class.module.merchant.showAllMerchant import showAllMerchant
def showOfSuperUser(loginUser=None):
    print("*" * 30 + "欢迎来到九江学院外卖平台----超级管理员界面" + "*" * 30)
    print("指令操作： 1.查看所有的用户       2.查看所有的商家        3.查看所有的店铺         4.查看所有的商品\n"
          "          5.查看所有的订单        6.退出登录")
    order = input("请输入你的指令:")
    while not re.match(r'[1-6]', order) or len(order) == 0 or len(order)>1:
        order = input(f"{order}值格式错误，请重新输入你的指令:")
    if order == "1":
        showAllUserAgain=showAllUser(loginUser=loginUser)
        while showAllUserAgain:
            showAllUserAgain = showAllUser(loginUser=loginUser)
    if order == "2":
        showAllMerchanterAgain=showAllMerchanter(loginUser=loginUser)
        while showAllMerchanterAgain:
            showAllMerchanterAgain = showAllMerchanter(loginUser=loginUser)
    if order == "3":
        showAllMerchantAgain =showAllMerchant(loginUser=loginUser)
        while showAllMerchantAgain:
            showAllMerchantAgain =showAllMerchant(loginUser=loginUser)
        pass
    if order == "4":
        showAllFoodAgain = showAllFood(loginUser=loginUser)
        while showAllFoodAgain:
            showAllFoodAgain =  showAllFood(loginUser=loginUser)
        pass
    if order == "5":
        showAllOrderAgain = showAllOrder(loginUser=loginUser)
        while showAllOrderAgain:
            showAllOrderAgain =showAllOrder(loginUser=loginUser)
        pass
    if order == "6":
        return False
    isAgain = input("是否继续操作?y/n")
    while not re.match(r'^[yYnN]*$', isAgain) or len(isAgain) == 0 or len(isAgain)>1:
        isAgain = input(f"{isAgain}值非法，是否继续操作?y/n")
    if isAgain == "y" or isAgain == "Y":
        return True
    else:
        return False