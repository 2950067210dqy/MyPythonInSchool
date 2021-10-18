import re
from shixun.overWork.Class.module.merchant.addMerchant import addMerchant
from shixun.overWork.Class.module.merchant.deleteMerchant import deleteMerchant
from shixun.overWork.Class.module.merchant.updateMerchant import updateMerchant
from shixun.overWork.Class.module.merchant.selectMerchant import selectMerchant
from shixun.overWork.Class.module.food.showFood import showFood
def showOfMerchanter(loginUser=None):

    print("*"*30+"欢迎来到九江学院外卖平台----商家界面"+"*"*30)
    print("查询中....")
    print("查询成功!")
    selectMerchant(loginUser=loginUser)
    print("店铺操作： 1.添加你的店铺          2.删除你的店铺         3.更新你的店铺      4.查看店铺的商品      5.退出登录")
    order=input("请输入你的指令:")
    while not re.match(r'[1-5]',order)   or len(order)==0 or len(order)>1:
        order=input(f"{order}值格式错误，请重新输入你的指令:")
    if order=="1":
        addMerchant(loginUser=loginUser)
    if order=="2":
        deleteMerchant(loginUser=loginUser)
    if order=="3":
        updateMerchant(loginUser=loginUser)
    if order == "4":
        merchantId=input("请输入你选择的店铺序号：")
        while not re.match(rf'[0-9]',merchantId) or len(merchantId)==0:
            merchantId = input(f"{merchantId}值格式错误，请重新输入你选择的店铺序号：")
        showFoodAgain=showFood(loginUser=loginUser,merchantId=int(merchantId))
        while showFoodAgain:
            merchantId = input("请输入你选择的店铺序号：")
            while not re.match(rf'[0-9]', merchantId) or len(merchantId) == 0:
                merchantId = input(f"{merchantId}值格式错误，请重新输入你选择的店铺序号：")
            showFoodAgain = showFood(loginUser=loginUser,merchantId=int(merchantId))
    if order=="5":
        return False
    isAgain = input("是否继续操作店铺?y/n")
    while not re.match(r'^[yYnN]*$', isAgain)  or len(isAgain)==0 or len(isAgain)>1:
        isAgain = input(f"{isAgain}值非法，是否继续操作店铺?y/n")
    if isAgain == "y" or isAgain == "Y":
        return True
    else:
        return False

