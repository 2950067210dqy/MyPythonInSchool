#邓亲优 20
print("-"*32)
print(" "*(32//2-4)+"注册界面")
name=input("请输入您的注册用户名：")
pw=input("请输入您的注册密码：")
print("恭喜您注册成功")
print("-"*32)
print("-"*32)
print(" "*(32//2-4)+"登录界面")
aname=input("请输入您的注册用户名：")
apw=input("请输入您的注册密码：")
if aname == name and apw == pw:
    print("登录成功!")
else:
    print("登录失败!")
print("-"*32)