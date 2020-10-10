#coding=utf-8

# 导入bmob模块
from bmob import *
# 新建一个bmob操作对象
b = Bmob("c4fa257e2e2ad9b9244ebd193505453a", "6897280cc0efff8604b6f1bba8a16b00")
# 插入一行数据，原子计数、Pointer
print(
	b.insert(
		'user', # 表名
		BmobUpdater.increment(
			"count", # 原子计数key
			3, # 原子计数值
			{ # 额外信息
                "username":"kkk",
                "password":"asd",
                "id":6
			}
		)
	).jsonData # 输出json格式的内容
)

print(
	b.find( # 查找数据库
		"user", # 表名
		BmobQuerier(). # 新建查询逻辑
			addWhereNotExists("user") # user不存在
		).stringData # 输出string格式的内容
)