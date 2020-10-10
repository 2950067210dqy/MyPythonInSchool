import pymysql
import tkinter as tk
#邓亲优 20
def button_clicked():
    listbox.delete(0,5)
    id=enrty1.get()
    if len(id) < 18 or len(id) > 18:
        label1["text"]=f"你输入的身份证号码'{id}'位数有误，请重新输入您的身份证号码(只支持18位身份证)"
        top.geometry("600x350")
        enrty1["width"]=50
        listbox["width"]=50
        enrty1.delete(0,len(id)+1)

    else:
        listbox.insert(0,"该人的身份信息如下：")
        db = pymysql.connect("127.0.0.1", "root", "")
        cursor = db.cursor()  # 数据游标
        cursor.execute("use peoplecard")  # 执行数据库sql语句
        cursor.execute("select * from smd_address_code")
        data = cursor.fetchall()  # data接收返回结果
        flag=True
        for i in range(0, len(data)):
            for j in range(0, len(data[i])):
                if id[0:6] in data[i][j]:
                    listbox.insert(1,f"您所在的城市为:{data[i][j + 1]}")
                    flag = False
                    break
        if (flag):
            listbox.insert(1, "您所在的城市为:未知")
        conn = "-"
        listbox.insert(2, f"出生日期：{conn.join([id[6:10], id[10:12], id[12:14]])}")
        if int(id[16:17]) % 2 == 1:
            listbox.insert(3, "性别：男")
        else:
            listbox.insert(3, "性别：女")
        listbox.insert(4, "-" * 32)
        star = "****"
        listbox.insert(5, f"身份证保密显示如下:{id[0:10] + star + id[14:18]}")
        top.geometry("600x350")
        enrty1["width"] = 50
        listbox["width"] = 50
        db.close()
top=tk.Tk()
top.title("身份证的秘密")
top.geometry("250x300")
label1=tk.Label(top,text="请输入您的身份证号码(只支持18位身份证)")
label1.pack()
enrty1=tk.Entry(top,width=20)
enrty1.pack()
listbox=tk.Listbox(top,width=20)
listbox.pack()
btn=tk.Button(top,text="查询",command=button_clicked,width=10)
btn.pack()
top.mainloop()




# id=input("请输入您的身份证号码(只支持18位身份证)")
# while len(id)<18 or len(id)>18:
#     id = input(f"你输入的身份证号码'{id}'位数有误，请重新输入您的身份证号码(只支持18位身份证)")
# print("-"*32)
# print("该人的身份信息如下：")
# db = pymysql.connect("127.0.0.1", "root", "")
# cursor = db.cursor()  # 数据游标
# cursor.execute("use peoplecard")  # 执行数据库sql语句
# cursor.execute("select * from smd_address_code")
# data = cursor.fetchall()  # data接收返回结果
# flag=True
# for i in range(0,len(data)):
#     for j in range(0,len(data[i])):
#         if id[0:6] in data[i][j]:
#             print(f"您所在的城市为:{data[i][j+1]}")
#             flag=False
#             break
# if(flag):
#     print("您所在的城市为：未知")
# conn="-"
# print(f"出生日期：{conn.join([id[6:10],id[10:12],id[12:14]])}")
# if int(id[16:17])%2==1:
#     print("性别：男")
# else:
#     print("性别：女")
# print("-"*32)
# star="****"
# print(f"身份证保密显示如下:{id[0:10]+star+id[14:18]}")
# db.close()