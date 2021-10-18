import time
from shixun.overWork.Class.pojo.Merchant import Merchant
from shixun.overWork.Class.IO.MerchantIO import MerchantIO
import re
def updateMerchant(loginUser=None):
    print("*" * 10 + "店铺更新模块" + "*" * 10)
    id = input("请输入您要更新的店铺序号：")
    while not re.match(r'[0-9]', id)  or len(id)==0:
        id = input(f"{id}值格式错误，请重新输入您要更新的店铺序号:")
    merchant = Merchant(id=int(id))
    mtio = MerchantIO(merchanter=loginUser, merchant=merchant.__dict__)
    maxid = mtio.getMaxId()
    while int(id) > (maxid - 1):
        id = input(f"暂未找到序号为{id}的店铺，请重新输入您要更新的店铺序号:")
    jsonData=mtio.selectById()
    # print(jsonData)
    # 店铺名
    isUpdateTitle=input(f"店铺名为{jsonData['title']},是否修改店铺名？y/n")
    while not re.match(r'[yYnN]',isUpdateTitle)  or len(isUpdateTitle)==0 or len(isUpdateTitle)>1:
        isUpdateTitle = input(f"{isUpdateTitle}值格式错误,店铺名为{jsonData['title']},是否修改店铺名？y/n")
    title=None
    if isUpdateTitle=='y' or isUpdateTitle== 'Y':
        title=input(f"您的旧店铺名为{jsonData['title']},请输入新的店铺名:")
    else:
        title=jsonData['title']
    # 店铺标签
    isUpdateTag = input(f"店铺标签为{jsonData['tag']},是否修改店铺标签？y/n")
    while not re.match(r'[yYnN]', isUpdateTag) or len(isUpdateTag)==0 or len(isUpdateTag)>1:
        isUpdateTag = input(f"{isUpdateTag}值格式错误,店铺标签为{jsonData['tag']},是否修改店铺标签？y/n")
    tag = None
    if isUpdateTag == 'y' or isUpdateTag == 'Y':
        tag = input(f"您的旧店铺标签为{jsonData['tag']},请输入新的店铺标签:")
    else:
        tag = jsonData['tag']
    time = jsonData['time']
    id = jsonData['id']
    merchanterId=jsonData['merchanterId']
    newMerchant=Merchant(id=id,title=title,tag=tag,time=time,merchanterId=merchanterId)
    mtio.merchant=newMerchant.__dict__
    mtio.updateById()
    print("更新成功")
    pass