class Merchanter:
    id=None
    username=None
    password=None
    perMission=None #权限
    charge=None  #当前用户金额
    def __init__(self,id=None,username=None,password=None,charge=5000):
       self.id=id
       self.username=username
       self.password=password
       self.perMission=2
       self.charge=charge
    # def getId(self):
    #     return self.id
    # def getUserName(self):
    #     return self.username
    # def getPassWord(self):
    #     return self.password
    # def getPerMission(self):
    #     return self.perMission
    # def getCharge(self):
    #     return self.charge
    # def setId(self,id=None):
    #     self.id=id
    #
    # def setUserName(self,username=None):
    #     self.username=username
    #
    # def setPassWord(self,password=None):
    #     self.password=password
    #
    # def setCharge(self,charge=None):
    #     self.charge=charge
    #
    #
    # def setPerMission(self,permission=2):
    #     self.perMission=permission
