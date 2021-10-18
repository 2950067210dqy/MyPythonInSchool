from shixun.overWork.Class.IO.AllUserIO import AllUserIO
from shixun.overWork.Class.pojo.Merchanter import Merchanter
import re
from shixun.overWork.Class.module.merchanter.addMerchanter import addMerchanter

def selectMerhcanter(loginUser=None):
    merchanter=Merchanter()
    io = AllUserIO(user=merchanter.__dict__)
    jsonData = io.getIO(pathIndex=io.user['perMission'])
    if len(jsonData) == 0:
        print("当前未有商家哦！快去添加吧！")
        isadd = input("是否添加商家？y/n")
        while not re.match(r'[yYnN]', isadd) or len(isadd) == 0 or len(isadd)>1:
            isadd = input(f"{isadd}值格式错误，是否添加商家？y/n")
        if isadd == 'y' or isadd == 'Y':
           addMerchanter(loginUser=loginUser)

    else:
        print("-" * 100)
        print(" " * 50 + f"商家信息表")
        print(" " * 4 + "序号" + " " * 4 + "用户名" + " " * 15 + "密码" + " " * 15 + "权限"+" "*8+"商家余额")
        for i in jsonData:
            print(
                " " * 4 + f"{i['id']}" + " " * 7 + f"{i['username']}" + " " * 22 + f"{i['password']}" + " " * 17 + f"{i['perMission']}"+" "*8+f"{i['charge']}")
        print("-" * 100)
    pass