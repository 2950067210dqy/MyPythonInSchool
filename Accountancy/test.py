import configparser
import os

# 用os模块来读取
curpath = os.path.dirname(os.path.realpath(__file__))

cfgpath = os.path.join(curpath, "setting.ini")  # 读取到本机的配置文件


# 调用读取配置模块中的类
conf = configparser.ConfigParser()

conf.read(cfgpath,encoding="utf-8-sig")

# 调用get方法，然后获取配置的数据
sender = conf.get("GUI", "title")
print(sender)

sub_conf = conf.options("GUI")
print(sub_conf)