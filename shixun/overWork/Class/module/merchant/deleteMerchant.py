import re
from shixun.overWork.Class.pojo.Merchant import Merchant
from shixun.overWork.Class.IO.MerchantIO import MerchantIO
from shixun.overWork.Class.pojo.Food import Food
from shixun.overWork.Class.IO.FoodIO import FoodIO
def deleteMerchant(loginUser=None):
    print("*" * 10 + "店铺删除模块" + "*" * 10)
    id=input("请输入您要删除的店铺序号：")
    while not re.match(r'[0-9]',id) or len(id)==0:
        id = input(f"{id}值格式错误，请重新输入您要删除的店铺序号:")
    merchant = Merchant(id=int(id))
    mtio = MerchantIO(merchanter=loginUser, merchant=merchant.__dict__)
    maxid=mtio.getMaxId()
    while int(id)>(maxid-1):
        id = input(f"暂未找到序号为{id}的店铺，请重新输入您要删除的店铺序号:")
    mtio.deleteById()
    #将级联的商品一并删除
    ftio=FoodIO(merchant=merchant.__dict__)
    jsonData=ftio.selectByMerchantId()
    for i in jsonData:
        food=Food(id=i['id'])
        ftio.food=food
        ftio.deleteById()
    print("删除成功！")
    pass