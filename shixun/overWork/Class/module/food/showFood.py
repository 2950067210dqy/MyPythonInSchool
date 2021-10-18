from shixun.overWork.Class.pojo.Merchant import Merchant
from shixun.overWork.Class.IO.MerchantIO import MerchantIO
from shixun.overWork.Class.module.food.selectFood import selefctFood
from shixun.overWork.Class.module.food.addFood import addFood
from shixun.overWork.Class.module.food.updateFood import updateFood
from shixun.overWork.Class.module.food.deleteFood import deleteFood
from shixun.overWork.Class.module.food.buyFood import buyFood
from shixun.overWork.Class.IO.AllUserIO import AllUserIO
from shixun.overWork.Class.pojo.Merchanter import Merchanter
import re
def showFood(loginUser=None,merchantId=None):
    merchant=Merchant(id=merchantId)
    mtio=MerchantIO(merchanter=loginUser,merchant=merchant.__dict__)


    #获得当前店铺
    jsonData=mtio.selectById()
    #判断选中的店铺是否是当前商家的
    if loginUser['id']!=jsonData['merchanterId'] and loginUser['perMission']==2:
        print("您输入的店铺序号不属于您的店铺，请重新输入")
        return True

    print( "*"*50+"欢迎来到商品模块"+"*"*50)
    selefctFood(loginUser=loginUser,merchant=jsonData)

    #普通用户
    if loginUser['perMission']==1:
        print("商品操作： 1.购买商品         2.返回店铺模块")
        order = input("请输入你的指令:")
        while not re.match(r'[1-2]', order) or len(order) == 0 or len(order)>1:
            order = input(f"{order}值格式错误，请重新输入你的指令:")
        if order == "1":
            buyFood(loginUser=loginUser, merchant=jsonData)
        if order == "2":
            print("正在返回店铺模块中....")
            print("返回成功")
            return False
        isAgain = input("是否继续浏览商品?y/n")
        while not re.match(r'^[yYnN]*$', isAgain) or len(isAgain) == 0:
            isAgain = input(f"{isAgain}值非法，是否继续浏览商品?y/n")
        if isAgain == "y" or isAgain == "Y":
            return True
        else:
            return False
    #商家
    elif loginUser['perMission']==2:
        print("商品操作： 1.添加商品          2.删除商品         3.更新商品      4.返回店铺模块")
        order = input("请输入你的指令:")
        while not re.match(r'[1-5]', order) or len(order)==0:
            order = input(f"{order}值格式错误，请重新输入你的指令:")
        if order == "1":
            addFood(loginUser=loginUser,merchant=jsonData)
        if order == "2":
           deleteFood(loginUser=loginUser,merchant=jsonData)
        if order == "3":
          updateFood(loginUser=loginUser,merchant=jsonData)
        if order == "4":
           print("正在返回店铺模块中....")
           print("返回成功")
           return False
        isAgain = input("是否继续操作商品?y/n")
        while not re.match(r'^[yYnN]*$', isAgain) or len(isAgain)==0 or len(isAgain)>1:
            isAgain = input(f"{isAgain}值非法，是否继续操作商品?y/n")
        if isAgain == "y" or isAgain == "Y":
            return True
        else:
            return False

        pass