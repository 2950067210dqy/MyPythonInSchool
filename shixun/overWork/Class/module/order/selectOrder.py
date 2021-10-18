from shixun.overWork.Class.IO.AllUserIO import AllUserIO
from shixun.overWork.Class.IO.MerchantIO import MerchantIO
from shixun.overWork.Class.IO.OrderIO import OrderIO
from shixun.overWork.Class.IO.FoodIO import FoodIO
from shixun.overWork.Class.pojo.Merchanter import Merchanter
from shixun.overWork.Class.pojo.User import User
from shixun.overWork.Class.pojo.Food import Food
from shixun.overWork.Class.pojo.Merchant import Merchant
from shixun.overWork.Class.pojo.Order import Order
import re
def selectOrder(loginUser=None):
    io=AllUserIO(user=loginUser)
    user=io.selectById()

    order=Order(userId=user['id'])
    orio=OrderIO(order=order.__dict__)
    orderList=None
    if loginUser['perMission']==3:
        orderList=orio.selectAll()
    else:
        orderList=orio.selectByUserId()
    if len(orderList) == 0:
        print("当前未有订单哦！快去购买吧！")
    else:
        print("-" * 130)
        if loginUser['perMission'] == 3:
            print(" "*60+f"订单表")
            print(" "*5+"序号"+" "*5+"用户"+" "*5+"商品"+" "*15+"单价"+" "*5+"数量"+" "*5+"总计"+" "*6+"所属店铺"+" "*15+"商家"+" "*7+"购买时间")
            for i in orderList:
               user=User(id=i['userId'])
               io=AllUserIO(user=user.__dict__)
               userThis=io.selectById()
               food=Food(id=i['foodId'])
               fdio=FoodIO(food=food.__dict__)
               foodThis=fdio.selectById()
               merchant=Merchant(id=foodThis['merchantId'])
               mtio=MerchantIO(merchant=merchant.__dict__)
               merchantThis=mtio.selectById()
               merchanter=Merchanter(id=merchantThis['merchanterId'])
               io=AllUserIO(user=merchanter.__dict__)
               merchanterThis=io.selectById()
               print(" "*5+f"{i['id']}"+" "*8+f"{userThis['username']}"+" "*8+f"{foodThis['title']}"+" "*15+f"￥{foodThis['price']}"+" "*5+f"{i['num']}"+" "*5+f"￥{int(foodThis['price'])*int(i['num'])}"+" "*6+f"{merchantThis['title']}"+" "*20+f"{merchanterThis['username']}"+" "*7+f"{i['time']}")
        else:
            print(" "*60+f"{loginUser['username']}的订单表")
            print(" "*5+"序号"+" "*5+"商品"+" "*15+"单价"+" "*5+"数量"+" "*5+"总计"+" "*6+"所属店铺"+" "*15+"商家"+" "*7+"购买时间")
            for i in orderList:
               food=Food(id=i['foodId'])
               fdio=FoodIO(food=food.__dict__)
               foodThis=fdio.selectById()
               merchant=Merchant(id=foodThis['merchantId'])
               mtio=MerchantIO(merchant=merchant.__dict__)
               merchantThis=mtio.selectById()
               merchanter=Merchanter(id=merchantThis['merchanterId'])
               io=AllUserIO(user=merchanter.__dict__)
               merchanterThis=io.selectById()
               print(" "*5+f"{i['id']}"+" "*8+f"{foodThis['title']}"+" "*15+f"￥{foodThis['price']}"+" "*5+f"{i['num']}"+" "*5+f"￥{int(foodThis['price'])*int(i['num'])}"+" "*6+f"{merchantThis['title']}"+" "*20+f"{merchanterThis['username']}"+" "*7+f"{i['time']}")
        print("-" * 130)


pass