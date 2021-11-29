import sys
import configparser
class configio:

    def __init__(self,url):
        self.config = configparser.ConfigParser()
        self.url=url
        self.config.read(url)
    def getsections(self):## 获得所有区域
        return self.config.sections()
        pass
    def getoptionsBysections(self,sections=[]):# 获取区域的所有key
        data={}
        for i in sections:
            data[i]=self.config.options(i)
        return data
        pass
    def getKeyValueBysections(self,sections=[]):# 获取区域的所有key value
        data = {}
        for i in sections:
            temp={}
            for j in self.config.items(i):
                temp[j[0]]=j[1]
            data[i]=temp
        return data
        pass
        pass
    def getValueBysectionAndKey(self,section,key):#根据section和key获取value
        return self.config.get(section,key)
        pass
    def checksection(self,section):#判断区域是否存在
        return self.config.has_section(section)
        pass