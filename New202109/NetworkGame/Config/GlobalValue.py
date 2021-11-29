import json

import logging as log
from New202109.NetworkGame.GameClass.IO.io import configio
import sys
class GlobalMap:
    # 拼装成字典构造全局变量  借鉴map  包含变量的增删改查
    map = {}
    mapconfig={}
    def __init__(self):
        url=sys.path[0] +"/Config/config.ini"
        io=configio(url=url)
        self.mapconfig=io.getKeyValueBysections(io.getsections())
        pass
    def set_map(self, key, value):
        if(isinstance(value,dict)):
            value = json.dumps(value)
        self.map[key] = value


    def set(self, keys):
        try:
            for key_, value_ in keys.items():
                self.map[key_] = str(value_)
                log.debug(key_+":"+str(value_))
        except BaseException as msg:
            log.error(msg)
            raise msg

    def del_map(self, key):
        try:
            del self.map[key]
            return self.map
        except KeyError:
            log.error("key:'" + str(key) + "'  不存在")


    def get(self,*args):
        try:
            dic = {}
            for key in args:
                if len(args)==1:
                    dic = self.map[key]
                    log.debug(key+":"+str(dic))
                elif len(args)==1 and args[0]=='all':
                    dic = self.map
                else:
                    dic[key]=self.map[key]
            return dic
        except KeyError:
            log.warning("key:'" + str(key) + "'  不存在")
            return 'Null_'
