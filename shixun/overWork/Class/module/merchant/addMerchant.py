import time
from shixun.overWork.Class.pojo.Merchant import Merchant
from shixun.overWork.Class.IO.MerchantIO import MerchantIO
def addMerchant(loginUser=None):

    print("*"*10+"店铺添加模块"+"*"*10)
    title=input("请输入您的店铺名:")
    tag=input("请输入您的店铺的标签")
    times=  time.strftime('%Y{y}%m{m}%d{d} %H{h}%M{f}%S{s}').format(y='年', m='月', d='日', h='时', f='分', s='秒')
    merchant= Merchant(title=title,tag=tag,time=times,merchanterId=loginUser['id'])
    mtio=MerchantIO(merchanter=loginUser,merchant=merchant.__dict__)
    if mtio.insertByMerchanterId():
        print("添加店铺成功")
    else:
        print("添加店铺失败")
    pass