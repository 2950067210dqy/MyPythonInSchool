import re
from shixun.overWork.Class.IO.AllUserIO import  AllUserIO

def addCharge(loginUser=None):
    print("*" * 10 + "金额充值模块" + "*" * 10)
    charging=input("你要充值多少元？")
    while not re.match(r'[0-9]',charging) or len(charging)>5:
        charging = input(f"{charging}格式错误，你要充值多少元？")
    loginUser['charge']=str(int(loginUser['charge'])+int(charging))
    io=AllUserIO(user=loginUser)
    io.updateById()
    print("充值成功！")
    return loginUser
    pass