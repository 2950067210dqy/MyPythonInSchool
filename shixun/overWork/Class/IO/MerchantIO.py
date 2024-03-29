import json

class MerchantIO:
    path="./database/merchant.json"
    merchanter=None
    merchant=None

    def __init__(self,merchanter=None,merchant=None):
        self.merchanter=merchanter
        self.merchant=merchant
        pass
    # 查询全部
    def selectAll(self):
        return self.getIO()
    def selectByMerchanterId(self):
        jsonData=self.getIO()
        newJsonData=[]
        for i in jsonData:
            if i['merchanterId']==self.merchanter['id']:
                newJsonData.append(i)
        return newJsonData
    def selectById(self):
        jsonData = self.getIO()
        newJsonData = None
        for i in jsonData:
            if i['id'] == self.merchant['id']:
                newJsonData=i
                break
        return newJsonData
    def insertByMerchanterId(self):
        # 判断是否存在同名店铺名
        if self.judgeRepeat():
            return False
        self.merchant["id"] = self.getMaxId()
        jsonData = self.getIO()
        jsonData.append(self.merchant)
        return self.set(jsonData=jsonData)
        pass

    def deleteById(self):
        jsonData=self.getIO()
        newJsonData=[]
        for i in jsonData:
            if i['id']==self.merchant['id']:
                continue
            newJsonData.append(i)
        self.set(newJsonData)
    def updateById(self):
        jsonData = self.getIO()
        newJsonData = []
        for i in jsonData:
            if i['id'] == self.merchant['id']:
                newJsonData.append(self.merchant)
                continue
            newJsonData.append(i)
        self.set(newJsonData)
    # 存储数据
    def set(self, jsonData=None):
        try:
            with open(self.path, 'w') as fp:
                json.dump(jsonData, fp)
            fp.close()
            return True
        except Exception:
            return False
    def getIO(self):
        with open(self.path, 'r', encoding='utf8')as fp:
            json_data = json.load(fp)
        fp.close()
        return json_data
    # 得到最大ID值
    def getMaxId(self):
        jsonData = self.getIO()
        id = []
        for i in jsonData:
            id.append(i["id"])
        if len(id) == 0:
            return 1
        else:
            return max(id) + 1
    # 判断用户是否重复
    def judgeRepeat(self):
        jsonData=self.getIO()
        for i in jsonData:
            if i['title']==self.merchant['title']:
                return True
        else:
            return False
        pass
