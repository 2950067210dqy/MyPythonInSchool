import pymysql
class curdDataBase:
    def __init__(self):
        pass
    # 连接数据库
    def connect(self,config):
        try:
            return pymysql.connect(host=config["host"],port=config["port"],user=config["user"],password=config["password"],database=config["database"],charset=config["charset"])
        except:
            return "数据库连接失败"
    # 获得游标
    def getCursor(self,db):
        return db.cursor()
    # 关闭数据库
    def close(self,db):
        return db.close()
    # 数据库回滚
    def rollback(self,db):
        return db.rollback()
    # 数据库提交
    def commit(self,db):
        return db.commit()
    # 语句执行
    def excute(self,cursor,sql,partm=""):
        return cursor.execute(sql,partm)