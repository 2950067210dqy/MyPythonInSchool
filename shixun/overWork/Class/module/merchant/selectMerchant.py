from shixun.overWork.Class.IO.MerchantIO import MerchantIO
from shixun.overWork.Class.IO.AllUserIO import AllUserIO
from shixun.overWork.Class.module.merchant.addMerchant import addMerchant
import re
def selectMerchant(loginUser=None):
    mtio=MerchantIO(merchanter=loginUser)
    jsonData=mtio.selectByMerchanterId()
    if len(jsonData)==0:
        print("当前未有店铺哦！快去添加吧！")
        isadd=input("是否添加店铺？y/n")
        while not re.match(r'[yYnN]',isadd)  or len(isadd)==0 or len(isadd)>1:
            isadd=input(f"{isadd}值格式错误，是否添加店铺？y/n")
        if isadd=='y' or isadd=='Y':
            addMerchant(loginUser=loginUser)

    else:
        print("-" * 100)
        print(" "*50+f"{loginUser['username']}的店铺表")
        print(" "*4+"序号"+" "*4+"店铺名"+" "*15+"店铺标签"+" "*15+"店铺创建时间")
        for i in jsonData:
            print(" "*4+f"{i['id']}"+" "*7+f"{i['title']}"+" "*17+f"{i['tag']}"+" "*17+f"{i['time']}")
        print("-" * 100)

