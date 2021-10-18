from shixun.overWork.Class.IO.AllUserIO import AllUserIO
from shixun.overWork.Class.pojo.User import User
from shixun.overWork.Class.IO.OrderIO import OrderIO
from shixun.overWork.Class.pojo.Order import Order
import re
def deleteUser(loginUser=None):
    print("*" * 10 + "用户删除模块" + "*" * 10)
    id = input("请输入您要删除的用户序号：")
    while not re.match(r'[0-9]', id) or len(id) == 0:
        id = input(f"{id}值格式错误，请重新输入您要删除的用户序号:")
    user = User(id=int(id))
    io = AllUserIO(user=user.__dict__)
    maxid = io.getMaxId()
    while int(id) > (maxid - 1):
        id = input(f"暂未找到序号为{id}的用户，请重新输入您要用户的序号:")
    io.deleteById()

    #级联删除订单
    order=Order(id=io.user['id'])
    orio=OrderIO(order=order.__dict__)
    orio.deleteById()

    print("删除成功！")
    pass