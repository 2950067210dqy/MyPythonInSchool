from shixun.overWork.Class.IO.AllUserIO import AllUserIO
from shixun.overWork.Class.pojo.Merchanter import Merchanter
from shixun.overWork.Class.pojo.Merchant import Merchant
from shixun.overWork.Class.pojo.Food import Food
from shixun.overWork.Class.IO.MerchantIO import MerchantIO
from  shixun.overWork.Class.IO.FoodIO import FoodIO
import re
def deleteMerchanter(loginUser=None):
    print("*" * 10 + "商家删除模块" + "*" * 10)
    id = input("请输入您要商家的用户序号：")
    while not re.match(r'[0-9]', id) or len(id) == 0:
        id = input(f"{id}值格式错误，请重新输入您要删除的商家序号:")
    merchanter = Merchanter(id=int(id))
    io = AllUserIO(user=merchanter.__dict__)
    maxid = io.getMaxId()
    while int(id) > (maxid - 1):
        id = input(f"暂未找到序号为{id}的商家，请重新输入您要商家的序号:")
    io.deleteById()

    # 级联删除店铺
    mtio=MerchantIO(merchanter=merchanter.__dict__)
    newMerchant=mtio.selectByMerchanterId()
    #如果有店铺
    if len(newMerchant)>0:
        mtio.merchant=newMerchant
        mtio.deleteById()
        # 将级联的商品一并删除
        for j in newMerchant:
            ftio = FoodIO(merchant=i)
            jsonData = ftio.selectByMerchantId()
            for i in jsonData:
                food = Food(id=i['id'])
                ftio.food = food
                ftio.deleteById()
    print("删除成功！")
    pass