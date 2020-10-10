#邓亲优 20

password="ix0678"
newpassword=""
for i in range(0,len(password)):
    #ord函数为将字符转换成ASCII码，chr函数将ASCII码转换为字符
    newpassword=newpassword+chr(ord(password[i])+5)
print(f"密码为{newpassword}")