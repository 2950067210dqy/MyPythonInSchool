import re
import time
from shixun.overWork.Class.IO.AllUserIO import AllUserIO
from shixun.overWork.Class.IO.OrderIO import OrderIO
from shixun.overWork.Class.pojo.User import User
from shixun.overWork.Class.pojo.Merchanter import Merchanter
from shixun.overWork.Class.pojo.Food import Food
from shixun.overWork.Class.pojo.Order import Order
from shixun.overWork.Class.IO.FoodIO import FoodIO
from shixun.overWork.Class.module.charge.addCharge import addCharge
def buyFood(loginUser=None,merchant=None):
    print("*" * 10 + "商品购买模块" + "*" * 10)
    id = input("请输入您要购买的商品序号：")
    while not re.match(r'[0-9]', id) or len(id) == 0:
        id = input(f"{id}值格式错误，请重新输入您要购买的商品序号:")
    food = Food(id=int(id))
    fdio = FoodIO(food=food.__dict__, merchant=merchant)
    maxid = fdio.getMaxId()
    while int(id) > (maxid - 1):
        id = input(f"暂未找到序号为{id}的商品，请重新输入您要购买的商品序号:")
    num=input("请输入您要购买的数量:")
    while not re.match(r'[0-9]',num) or len(num)==0:
        num = input(f"{num}值格式错误，请重新输入您要购买的数量:")
    chooseFood=fdio.selectById()
    allPrice=int(chooseFood['price'])*int(num)
    isBuy=input(f"您购买的商品为：{chooseFood['title']}，单价为：{chooseFood['price']}元，数量为：{num}件，总价为：{allPrice}元，是否购买？y/n")
    while not re.match(r'[yYnN]',isBuy) or len(isBuy)==0:
        isBuy = input(
            f"{isBuy}值格式错误,您购买的商品为：{chooseFood['title']}，单价为：{chooseFood['price']}元，数量为：{num}件，总价为：{allPrice}元，是否购买？y/n")
    if isBuy=='y' or isBuy=='Y':
        while int(loginUser['charge'])<allPrice:
            isSpend=input(f"您的账户余额为￥{loginUser['charge']},余额不足，是否充值？y/n")
            while not re.match(r'[YyNn]',isSpend):
                isSpend = input(f"{isSpend}值格式错误，您的账户余额为￥{loginUser['charge']},余额不足，是否充值？y/n")
            if isSpend =='y' or isSpend =='Y':
                loginUser=addCharge(loginUser=loginUser)
            else:
                print("取消充值！")
                print("取消购买！")
                return
        #当前用户余额减少，商家余额增加
        loginUser['charge'] = str(int(loginUser['charge']) -int(allPrice))
        io = AllUserIO(user=loginUser)
        io.updateById()

        newMerchant=Merchanter(id=merchant['merchanterId'])
        io2=AllUserIO(user=newMerchant.__dict__)
        merchanter=io2.selectById()
        merchanter['charge']=str(int(merchanter['charge'])+int(allPrice))
        io2.user=merchanter
        io2.updateById()

        times = time.strftime('%Y{y}%m{m}%d{d} %H{h}%M{f}%S{s}').format(y='年', m='月', d='日', h='时', f='分', s='秒')
        order=Order(userId=loginUser['id'],foodId=chooseFood['id'],num=num,time=times)
        orio=OrderIO(order=order.__dict__)
        orio.insert()
        print(f"购买成功！账户余额为￥{loginUser['charge']}")
    else:
        print("取消购买！")

    pass