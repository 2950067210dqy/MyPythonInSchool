from shixun.overWork.Class.module.merchanter.selectMerchanter import selectMerhcanter
from shixun.overWork.Class.module.merchanter.updateMerchanter import updateMerchanter
from shixun.overWork.Class.module.merchanter.addMerchanter import addMerchanter
from shixun.overWork.Class.module.merchanter.deleteMerchanter import deleteMerchanter
import re
def showAllMerchanter(loginUser=None):
    print("*" * 30 + "欢迎来到九江学院外卖平台----商家信息界面" + "*" * 30)
    print("查询中....")
    print("查询成功!")
    selectMerhcanter(loginUser=loginUser)
    print("用户操作： 1.删除商家       2.增加商家         3.编辑商家          4.返回上一级")
    order = input("请输入你的指令:")
    while not re.match(r'[1-4]', order) or len(order) == 0 or len(order)>1:
        order = input(f"{order}值格式错误，请重新输入你的指令:")
    if order == "1":
       deleteMerchanter(loginUser=loginUser)
    if order == "2":
       addMerchanter(loginUser=loginUser)
    if order == "3":
       updateMerchanter(loginUser=loginUser)
    if order == "4":
        return False
    isAgain = input("是否继续操作商家信息?y/n")
    while not re.match(r'^[yYnN]*$', isAgain) or len(isAgain) == 0 or len(isAgain)>1:
        isAgain = input(f"{isAgain}值非法，是否继续操作商家信息?y/n")
    if isAgain == "y" or isAgain == "Y":
        return True
    else:
        return False

    pass