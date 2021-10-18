class Order:
    id=None
    userId=None
    # foods=[]#点的食物包装类 orderFoods对象
    foodId=None
    num=None
    time=None
    # state=None #订单状态 0 未付款 1 已付款
    def __init__(self,id=None,userId=None,foodId=None,time=None,num=None,state=None):
        self.id=id
        self.userId=userId
        self.foodId=foodId
        self.num=num
        self.time=time
        # self.state=state
    # def getId(self):
    #     return self.id
    # def getUserId(self):
    #     return self.userId
    # def getFoods(self):
    #     return self.foods
    # def getState(self):
    #     return self.state
    # def getTime(self):
    #     return self.time
    # def setId(self,id=None):
    #     self.id=id
    # def setUserId(self,userId=None):
    #     self.userId=userId
    # def setTime(self,time=None):
    #     self.time=time
    # def setState(self,state=None):
    #     self.state=state
    # def setTime(self,time=None):
    #     self.time=time
# class OrderFoods:
#     id =None
#     merchanterId=None#商家id
#     merchantId=None#店铺id
#     food=None #food对象
#     num=None  #数量
#     def __init__(self,id=None,merchanterId=None,merchantId=None,food=None,num=None):
#         self.id=id
#         self.merchanterId=merchanterId
#         self.merchantId=merchantId
#         self.food=food
#         self.num=num
#         pass
    #
    # def getId(self):
    #     return self.id
    # def getMerchanterId(self):
    #     return self.merchanterId
    # def getMerchantId(self):
    #     return self.merchantId
    # def getFood(self):
    #     return self.food
    # def getNum(self):
    #     return self.num
    # def setId(self,id=None):
    #     self.id=id
    # def setMerchanterId(self,merchanterId=None):
    #     self.merchanterId=merchanterId
    # def setMerchantId(self,merchantId=None):
    #     self.merchantId=merchantId
    # def setFood(self,food=None):
    #     self.food=food
    # def setNum(self,num=None):
    #     self.num=num