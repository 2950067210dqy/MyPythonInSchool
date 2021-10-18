# 专门用来的连接存储单词库的数据库操作类
from GuessWords.GuessWordsClass.CurdDataBase import curdDataBase
class curdDataBaseAdptorByGuessWords:
    config={
    "host":"localhost",
    "port":3306,
    "user":"root",
    "password":"",
    "database":"guesswords",
    "charset":"utf8"
    }
    curddatabase=None
    def __init__(self):
        self.curddatabase=curdDataBase()
    def connectDataBase(self):
        return self.curddatabase.connect(config=self.config)
    def getCursor(self,db):
        return self.curddatabase.getCursor(db=db)
    # 关闭数据库
    def close(self, db):
        return self.curddatabase.close(db)
    # 数据库回滚
    def rollback(self, db):
        return self.curddatabase.rollback(db)
    # 数据库提交
    def commit(self, db):
        return self.curddatabase.commit(db)
    # 创建数据库
    def createDataBase(self,cursor):
        sql="""
        CREATE DATABASE IF NOT EXISTS `guesswords` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
        """
        return self.curddatabase.excute(cursor=cursor, sql=sql, partm=())
    # 创建表
    def createTable(self,cursor):
        sql="""
        CREATE TABLE IF NOT EXISTS `guesswords`.`words` (
        `id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY ,
        `word` VARCHAR( 100 ) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL ,
        `translate` VARCHAR( 100 ) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL ,
        `insert_time` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ,
        INDEX ( `word` , `translate` , `insert_time` )
        ) ENGINE = INNODB;
        """
        return self.curddatabase.excute(cursor=cursor,sql=sql,partm=())
    # 插入
    def insert(self,cursor,partm):
        sql="""
        insert into words values(null,%s,'',null)
        """
        return self.curddatabase.excute(cursor=cursor,sql=sql,partm=(partm))
    # 查询所有
    def selectAll(self,cursor):
        sql="""
        select * from words
        """
        return self.curddatabase.excute(cursor=cursor,sql=sql,partm=())
    # 删除所有
    def deleteAll(self,cursor):
        sql="""
        delete from words
        """
        return self.curddatabase.excute(cursor=cursor, sql=sql, partm=())