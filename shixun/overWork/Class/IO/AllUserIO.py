import json

class AllUserIO:
    path={1:"./database/user.json",2:"./database/merchanter.json",3:"./database/superUser.json",4:"./database/loginUser.json"}
    user=None
    def __init__(self,user=None):
        self.user=user
        pass
    #存储数据
    def set(self,jsonData=None,pathIndex=None):
        try:
            with open(self.path[pathIndex], 'w') as fp:
                json.dump(jsonData, fp)
            fp.close()
            return True
        except Exception:
            return False
    #存储数据[注册存储]
    def setByRegist(self):
        # 判断是否存在该账号
        if self.judgeRepeat():
            return False
        self.user["id"]=self.getMaxId()
        jsonData=self.getIO(pathIndex=self.user['perMission'])
        jsonData.append(self.user)
        return self.set(jsonData=jsonData,pathIndex=self.user['perMission'])
    #获得数据
    def getIO(self,pathIndex=None):
        with open(self.path[pathIndex], 'r', encoding='utf8')as fp:
            json_data = json.load(fp)
        fp.close()
        return json_data
    #得到最大ID值
    def getMaxId(self):
        jsonData = self.getIO(pathIndex=self.user['perMission'])
        id=[]
        for i in jsonData:
            id.append(i["id"])
        if len(id)==0:
            return 1
        else:
            return max(id)+1
    #判断用户是否重复
    def judgeRepeat(self):
        jsonData = self.getIO(pathIndex=self.user['perMission'])
        for i in jsonData:
            if self.user['username']==i["username"]:
                return True
        else:
            return False
    #登录
    def login(self):
        jsonData = self.getIO(pathIndex=self.user['perMission'])
        for i in jsonData:
            if self.user['username']==i['username'] and self.user['password'] == i['password']:
                self.set(jsonData=i,pathIndex=4)
                return True
        else:
            return False
    #更新密码
    def updatePasswordByUsername(self):
        jsonData = self.getIO(pathIndex=self.user['perMission'])
        index=None
        for i in range(len(jsonData)):
            if self.user['username'] == jsonData[i]['username'] :
               index=i
               break
        jsonData[index]['password']=self.user['password']
        self.set(jsonData=jsonData,pathIndex=self.user['perMission'])
    def updateById(self):
        jsonData = self.getIO(pathIndex=self.user['perMission'])
        newJsonData=[]
        for i in jsonData:
            if i['id']==self.user['id']:
                newJsonData.append(self.user)
                continue
            newJsonData.append(i)
        self.set(jsonData=newJsonData, pathIndex=self.user['perMission'])
    def selectById(self):
        jsonData = self.getIO(pathIndex=self.user['perMission'])
        newJsonData=None
        for i in jsonData:
            if i['id']==self.user['id']:
                newJsonData=i
                break
        return newJsonData
    def deleteById(self):
        jsonData = self.getIO(pathIndex=self.user['perMission'])
        newJsonData = []
        for i in jsonData:
            if i['id'] == self.user['id']:
                continue
            newJsonData.append(i)
        self.set(newJsonData)
