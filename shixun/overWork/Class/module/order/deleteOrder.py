from shixun.overWork.Class.pojo.Order import Order
from shixun.overWork.Class.IO.OrderIO import OrderIO
import re
def deleteOrder(loginUser=None):
    print("*" * 10 + "订单删除模块" + "*" * 10)
    id = input("请输入您要订单的店铺序号：")
    while not re.match(r'[0-9]', id) or len(id) == 0:
        id = input(f"{id}值格式错误，请重新输入您要删除的订单序号:")
    order = Order(id=int(id))
    orio = OrderIO(order=order.__dict__)
    maxid = orio.getMaxId()
    while int(id) > (maxid - 1):
        id = input(f"暂未找到序号为{id}的订单，请重新输入您要删除的订单序号:")
    orio.deleteById()
    print("删除成功！")
    pass