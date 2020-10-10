#邓亲优20
numb=input("请输入您的学号")
while len(numb)>12 or len(numb)<12:
    numb = input("您输入的学号位数不对，请重新输入您的学号")
if numb[4:8] == "6511":
    print(f"学号为{numb}的学生是网络资源系的学生！")
else:
    print(f"学号为{numb}的学生是学生！")