from shixun.overWork.Class.IO.AllUserIO import AllUserIO
from shixun.overWork.Class.pojo.Merchanter import Merchanter
import re
def updateMerchanter(loginUser=None):
    print("*" * 10 + "商家更新模块" + "*" * 10)
    id = input("请输入您要更新的商家序号：")
    while not re.match(r'[0-9]', id) or len(id) == 0:
        id = input(f"{id}值格式错误，请重新输入您要更新的商家序号:")
    merchanter = Merchanter(id=int(id))
    io = AllUserIO(user=merchanter.__dict__)
    maxid = io.getMaxId()
    while int(id) > (maxid - 1):
        id = input(f"暂未找到序号为{id}的商家，请重新输入您要更新的商家序号:")
    jsonData = io.selectById()
    # print(jsonData)
    isUpdateUsername = input(f"账号为{jsonData['username']},是否修改账号？y/n")
    while not re.match(r'[yYnN]', isUpdateUsername) or len(isUpdateUsername) == 0:
        isUpdateUsername = input(f"{isUpdateUsername}值格式错误,账号为{jsonData['username']},是否修改账号？y/n")
    username = None
    if isUpdateUsername == 'y' or isUpdateUsername == 'Y':
        username = input(f"旧账号为{jsonData['username']},请输入新账号:")
    else:
        username = jsonData['username ']

    isUpdatePassword = input(f"密码为{jsonData['password']},是否修改密码？y/n")
    while not re.match(r'[yYnN]', isUpdatePassword) or len(isUpdatePassword) == 0:
        isUpdatePassword = input(f"{isUpdatePassword}值格式错误,密码为{jsonData['password']},是否修改密码？y/n")
    password = None
    if isUpdatePassword == 'y' or isUpdatePassword == 'Y':
        password = input(f"旧密码为{jsonData['password']},请输入新密码:")
    else:
        password = jsonData['password']

    isUpdateCharge = input(f"余额为￥为{jsonData['charge']},是否修改余额？y/n")
    while not re.match(r'[yYnN]', isUpdateCharge) or len(isUpdateCharge) == 0:
        isUpdateCharge = input(f"{isUpdateCharge}值格式错误,余额为￥{jsonData['charge']},是否修改余额？y/n")
    charge = None
    if isUpdateCharge == 'y' or isUpdateCharge == 'Y':
        charge = input(f"旧余额为￥{jsonData['charge']},请输入新余额￥:")
    else:
        charge = jsonData['charge']
    newMerchanter =Merchanter(id=jsonData['id'], username=username, password=password, charge=charge)
    io.user = newMerchanter .__dict__
    io.updateById()
    print("更新成功")
    pass