import re
from shixun.overWork.Class.IO.MerchantIO import MerchantIO
from shixun.overWork.Class.IO.AllUserIO import AllUserIO
from  shixun.overWork.Class.pojo.Merchanter import Merchanter
from shixun.overWork.Class.module.merchant.addMerchant import addMerchant
def selectAllMerchant(loginUser=None):
    mtio=MerchantIO(merchanter=loginUser)
    jsonData=mtio.selectAll()
    if len(jsonData)==0:
        print("当前未有店铺哦！")
    else:
        print("-" * 100)
        print(" "*25+"九江学院外卖店铺")
        print(" "*4+"序号"+" "*4+"店铺名"+" "*15+"店铺标签"+" "*15+"店铺创建时间"+" "*30+"商家")
        for i in jsonData:
            merchanter=Merchanter(id=i['merchanterId'])
            io=AllUserIO(user=merchanter.__dict__)
            newMerchanter=io.selectById()
            print(" "*4+f"{i['id']}"+" "*7+f"{i['title']}"+" "*17+f"{i['tag']}"+" "*17+f"{i['time']}"+" "*15+f"{newMerchanter['username']}")
        print("-" * 100)