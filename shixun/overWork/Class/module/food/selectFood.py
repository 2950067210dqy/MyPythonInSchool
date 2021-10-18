from shixun.overWork.Class.IO.FoodIO import FoodIO
from shixun.overWork.Class.module.merchant.addMerchant import addMerchant
from shixun.overWork.Class.pojo.Food import Food
from shixun.overWork.Class.module.food.addFood import addFood
from shixun.overWork.Class.pojo.Merchant import Merchant
from shixun.overWork.Class.pojo.Merchanter import Merchanter
from shixun.overWork.Class.IO.MerchantIO import MerchantIO
from shixun.overWork.Class.IO.AllUserIO import AllUserIO
import re
def selefctFood(loginUser=None,merchant=None):
    print("查询商品中，请稍后.....")
    food=None
    fdio=None
    jsonData=None
    if loginUser['perMission']==3:
        fdio=FoodIO()
        jsonData=fdio.selectAll()
    else:
        food=Food(merchantId=merchant['id'])
        fdio = FoodIO(food=food,merchant=merchant)
        jsonData = fdio.selectByMerchantId()
    print("查询成功")
    if len(jsonData) == 0:

        if loginUser['perMission']==2:
            print(f"当前店铺[{merchant['title']}]未有商品哦！快去添加吧！")
            isadd = input("是否添加商品？y/n")
            while not re.match(r'[yYnN]', isadd) or len(isadd)==0 or len(isadd)>1:
                isadd = input(f"{isadd}值格式错误，是否添加商品？y/n")
            if isadd == 'y' or isadd == 'Y':
                addFood(loginUser=loginUser,merchant=merchant)
                selefctFood(loginUser=loginUser,merchant=merchant)
        else:
            print(f"当前店铺[{merchant['title']}]未有商品哦！去其他店铺看看吧！")
    else:
        print("-" * 130)
        if loginUser['perMission'] == 3:
            print(" "*40+f"商品表")
            print(" " * 4 + "序号" + " " * 4 + "商品名" +" " * 4 + "商品价格" + " " * 15 + "商品标签" + " " * 15 +"所属店铺"+" "*15+"所属商家"+" "*15+ "商品创建时间")
            for i in jsonData:
                merchant=Merchant(id=i['merchantId'])
                mtio=MerchantIO(merchant=merchant.__dict__)
                merchantThis=mtio.selectById()
                merchanter=Merchanter(id=merchantThis['merchanterId'])
                io=AllUserIO(user=merchanter.__dict__)
                merchanterThis=io.selectById()

                print(
                    " " * 4 + f"{i['id']}" + " " * 7 + f"{i['title']}"  + " " * 7 + f"￥{i['price']}" + " " * 17 + f"{i['tag']}" + " " * 17 + f"{merchantThis['title']}" + " " * 17 + f"{merchanterThis['username']}" + " " * 17 + f"{i['time']}")
        else:
            print(" "*40+f"店铺：{merchant['title']}的商品表")
            print(" " * 4 + "序号" + " " * 4 + "商品名" +" " * 4 + "商品价格" + " " * 15 + "商品标签" + " " * 15 + "商品创建时间")
            for i in jsonData:
                print(
                    " " * 4 + f"{i['id']}" + " " * 7 + f"{i['title']}"  + " " * 7 + f"￥{i['price']}" + " " * 17 + f"{i['tag']}" + " " * 17 + f"{i['time']}")
        print("-" * 130)
