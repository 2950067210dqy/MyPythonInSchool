class Merchant:
    id=None
    title=None
    time=None
    tag = None
    merchanterId=None # 商家ID
    def __init__(self,id=None,title=None,time=None,merchanterId=None,tag=None):
        self.id=id
        self.title=title
        self.time=time
        self.merchanterId=merchanterId
        self.tag=tag
    # def getId(self):
    #     return self.id
    # def getTitle(self):
    #     return self.title
    # def getTag(self):
    #     return self.tag
    # def getTime(self):
    #     return self.time
    # def getFoods(self):
    #     return self.foods
    # def setId(self,id=None):
    #     self.id=id
    # def setTitle(self,title=None):
    #     self.title=title
    # def setTag(self,tag=None):
    #     self.tag=tag
    # def setTime(self,time=None):
    #     self.price=time
    # def setFoods(self,foods=[]):
    #     self.foods=foods