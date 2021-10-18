import time
from shixun.overWork.Class.pojo.Food import Food
from shixun.overWork.Class.IO.FoodIO import FoodIO
import re
def addFood(loginUser=None,merchant=None):
    print("*" * 10 + "商品添加模块" + "*" * 10)
    title = input("请输入您的商品名:")
    tag = input("请输入您的商品的标签：")
    price =input("请输入您的商品的价格：")
    while not re.match(r'[0-9]',price) or len(price)==0:
        price = input(f"{price}值格式有误，请重新输入您的商品的价格：")
    times = time.strftime('%Y{y}%m{m}%d{d} %H{h}%M{f}%S{s}').format(y='年', m='月', d='日', h='时', f='分', s='秒')

    food = Food(title=title, tag=tag, time=times,price=price, merchantId=merchant['id'])
    fdio = FoodIO(food=food.__dict__, merchant=merchant)
    if fdio.insertByMerchantId():
        print("添加商品成功")
    else:
        print("添加商品失败")
    pass
