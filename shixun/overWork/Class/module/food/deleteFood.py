import re
from shixun.overWork.Class.pojo.Food import Food
from shixun.overWork.Class.IO.FoodIO import FoodIO
def deleteFood(loginUser=None,merchant=None):
    print("*" * 10 + "商品删除模块" + "*" * 10)
    id = input("请输入您要删除的商品序号：")
    while not re.match(r'[0-9]', id) or len(id)==0:
        id = input(f"{id}值格式错误，请重新输入您要删除的商品序号:")
    food =Food(id=int(id))
    fdio = FoodIO(food=food.__dict__, merchant=merchant)
    maxid=fdio.getMaxId()
    while int(id)>(maxid-1):
        id = input(f"暂未找到序号为{id}的商品，请重新输入您要删除的商品序号:")
    fdio.deleteById()
    print("删除成功！")
    pass