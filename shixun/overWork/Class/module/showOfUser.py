from shixun.overWork.Class.module.merchant.selectAllMerchant import selectAllMerchant
from shixun.overWork.Class.module.food.showFood import showFood
from shixun.overWork.Class.module.charge.showCharge import showCharge
from shixun.overWork.Class.module.charge.addCharge import addCharge
from shixun.overWork.Class.module.order.showOrder import showOrder
import re
def showOfUser(loginUser=None):
    print("*" * 30 + "欢迎来到九江学院外卖平台----用户界面" + "*" * 30)
    print("查询中....")
    print("查询成功!")
    selectAllMerchant(loginUser=loginUser)
    print("店铺操作： 1.查看店铺的商品       2.查看你的余额        3.充值余额         4.查看订单      5.退出登录")
    order = input("请输入你的指令:")
    while not re.match(r'[1-5]', order) or len(order) == 0 or len(order)>1:
        order = input(f"{order}值格式错误，请重新输入你的指令:")
    if order == "1":
        merchantId = input("请输入你选择的店铺序号：")
        while not re.match(r'[0-9]', merchantId) or len(merchantId) == 0:
            merchantId = input(f"{merchantId}值格式错误，请重新输入你选择的店铺序号：")
        showFoodAgain = showFood(loginUser=loginUser, merchantId=int(merchantId))
        while showFoodAgain:
            showFoodAgain = showFood(loginUser=loginUser, merchantId=int(merchantId))
    if order == "2":
        print(f"您当前的余额为：￥{showCharge(loginUser=loginUser)}")
    if order == "3":
        loginUser=addCharge(loginUser=loginUser)
        pass
    if order == "4":
        showOrderAgain=showOrder(loginUser=loginUser)
        while showOrderAgain:
            showOrderAgain = showOrder(loginUser=loginUser)
    if order == "5":
       return False
    isAgain = input("是否继续浏览店铺?y/n")
    while not re.match(r'^[yYnN]*$', isAgain) or len(isAgain) == 0 or len(isAgain)>1:
        isAgain = input(f"{isAgain}值非法，是否继续浏览店铺?y/n")
    if isAgain == "y" or isAgain == "Y":
        return True
    else:
        return False