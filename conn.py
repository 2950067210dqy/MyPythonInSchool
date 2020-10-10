import pymysql
db = pymysql.connect("127.0.0.1", "root", "")

cursor = db.cursor()  # 数据游标