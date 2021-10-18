import configparser
import os
class Setting():
    cfgpath=os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), "setting.ini")  # 读取配置文件路径
    def __init__(self):
        # 调用读取配置模块中的类
        self.conf = configparser.ConfigParser()
        self.conf.read(self.cfgpath, encoding="utf-8-sig")
        pass
    def getGUISetting(self):
        # 将配置的值取出来放到字典里并返回
        GUIOption={}
        sub_conf = self.conf.options("GUI")
        for i in sub_conf:
            GUIOption[i]= self.conf.get("GUI", i)
        return GUIOption
        pass