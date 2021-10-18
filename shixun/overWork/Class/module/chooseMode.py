from shixun.overWork.Class.module.login import login
from shixun.overWork.Class.module.regist import register

import re
def chooseMode():
    print("1.登录" + " " * 10 + "2.注册")
    inputChoose = input("请选择您要操作的模式:")
    while not re.match(r'^[1-2]*$', inputChoose) or len(inputChoose)==0 or len(inputChoose)>1:
        inputChoose = input(f"{inputChoose}值非法，请重新你要操作的模式:")

    if int(inputChoose) == 2:
        # 注册
        registerAgain=register()
        while registerAgain:
            registerAgain = register()
        pass
 # 登录
    loginAgain=login()
    while not loginAgain :
        loginAgain = login()
