import sys

from New202109.NetworkGame.GameClass.Main.thread import Main
from New202109.NetworkGame.Config.Logging import loggings
from New202109.NetworkGame.Config.GlobalValue import GlobalMap
import logging



if __name__ == '__main__':
    # 全局变量初始化
    GlobalMap()
    print(GlobalMap().mapconfig)
    #日志类初始化
    loggingConfigPath = sys.path[0] + GlobalMap().mapconfig['path']['baseconfigpath']+GlobalMap().mapconfig['filename']['loggingname']
    loggings(loggingConfigPath=loggingConfigPath)



    go=Main()
    go.start()

