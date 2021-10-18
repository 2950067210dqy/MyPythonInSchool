import re
from shixun.overWork.Class.pojo.Food import Food
from shixun.overWork.Class.IO.FoodIO import FoodIO
def updateFood(loginUser=None,merchant=None):
    print("*" * 10 + "商品更新模块" + "*" * 10)
    id = input("请输入您要更新的商品序号：")
    while not re.match(r'[0-9]', id) or len(id)==0:
        id = input(f"{id}值格式错误，请重新输入您要更新的商品序号:")
    food = Food(id=int(id))
    fdio =FoodIO(food=food.__dict__, merchant=merchant)
    maxid =fdio.getMaxId()
    while int(id) > (maxid - 1):
        id = input(f"暂未找到序号为{id}的商品，请重新输入您要更新的商品序号:")
    jsonData = fdio.selectById()

    # 商品名
    isUpdateTitle = input(f"商品名为{jsonData['title']},是否修改商品名？y/n")
    while not re.match(r'[yYnN]', isUpdateTitle) or len(isUpdateTitle)==0 or len(isUpdateTitle)>1:
        isUpdateTitle = input(f"{isUpdateTitle}值格式错误,商品名为{jsonData['title']},是否修改商品名？y/n")
    title = None
    if isUpdateTitle == 'y' or isUpdateTitle == 'Y':
        title = input(f"您的旧商品名为{jsonData['title']},请输入新的商品名:")
    else:
        title = jsonData['title']
    # 商品标签
    isUpdateTag = input(f"商品标签为{jsonData['tag']},是否修改商品标签？y/n")
    while not re.match(r'[yYnN]', isUpdateTag) or len(isUpdateTag)==0 or len(isUpdateTag)>1:
        isUpdateTag = input(f"{isUpdateTag}值格式错误,商品标签为{jsonData['tag']},是否修改商品标签？y/n")
    tag = None
    if isUpdateTag == 'y' or isUpdateTag == 'Y':
        tag = input(f"您的旧商品标签为{jsonData['tag']},请输入新的商品标签:")
    else:
        tag = jsonData['tag']
    # 商品价格
    isUpdatePrice = input(f"商品价格为￥{jsonData['price']},是否修改价格？y/n")
    while not re.match(r'[yYnN]', isUpdatePrice) or len(isUpdatePrice)==0 or len(isUpdatePrice)>1:
        isUpdatePrice = input(f"{isUpdatePrice}值格式错误,商品价格为￥{jsonData['price']},是否修改价格？y/n")
    price = None
    if isUpdatePrice == 'y' or isUpdatePrice == 'Y':
        price = input(f"您的旧商品价格为￥{jsonData['price']},请输入新的商品价格:")
        while not re.match(r'[0-9]', price) or len(price)==0:
            price = input(f"{price}值格式有误，请重新输入您的商品的价格：")
    else:
        price = jsonData['price']
    time = jsonData['time']
    id = jsonData['id']
    merchantId = jsonData['merchantId']
    newFood = Food(id=id, title=title, tag=tag, time=time, merchantId=merchantId,price=price)
    fdio.food = newFood.__dict__
    fdio.updateById()
    print("更新成功")
    pass