# import pymysql
# db = pymysql.connect("127.0.0.1", "root", "")
# cursor = db.cursor()  # 数据游标
# cursor.execute("use peoplecard")  # 执行数据库sql语句
# cursor.execute("select * from smd_address_code")
# data = cursor.fetchall()  # data接收返回结果
# print(data)
#
# db.close()  # 关闭数据库


# class Pet:
#     def __init__(self,name,weight):
#         self.name=name;
#         self.weight=weight;
#         print(f"您好我的名字是{name},很高兴认识你！我的体重为{weight}克")
#     def eat(self,food):
#         if food=='hotdog':
#             print("热狗真好吃！")
#             self.weight=self.weight+10
#         self.weight=self.weight+2
#         print('真开心给我吃的')
#     def checkWeight(self):
#         if self.weight>20:
#             print("我有点超重了呢")
#         else:
#             print("我很健康呢")
# p1=Pet('垃圾',0)
# p1.eat("hotdog")
# p1.eat("shi")
# p1.checkWeight()
s1='s'


print(type(s1))
