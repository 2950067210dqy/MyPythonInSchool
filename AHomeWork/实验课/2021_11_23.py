import re
import json
import time
class Student:
    id=None
    name=None
    age=None
    class_grade=None
    id_card=None
    address=None
    time=None
    def __init__(self,id=None,name=None,age=None,class_grade=None,id_card=None,address=None,time=None):
        self.id=id;
        self.name=name
        self.age=age
        self.class_grade=class_grade
        self.id_card=id_card
        self.address=address
        self.time=time
        pass



class AllStudentIO:
    path="./student.json"
    student=None
    def __init__(self,student=None):
        self.student=student
        pass
    #存储数据
    def set(self,jsonData=None):
        try:
            with open(self.path, 'w') as fp:
                json.dump(jsonData, fp)
            fp.close()
            return True
        except Exception:
            return False
    #获得数据
    def getIO(self):
        with open(self.path, 'r', encoding='utf8')as fp:
            json_data = json.load(fp)
        fp.close()
        return json_data
    #得到最大ID值
    def getMaxId(self):
        jsonData = self.getIO()
        id=[]
        for i in jsonData:
            id.append(i["id"])
        if len(id)==0:
            return 1
        else:
            return max(id)+1
    #判断用户是否重复
    def judgeRepeat(self):
        jsonData = self.getIO()
        for i in jsonData:
            if self.student['id_card']==i["id_card"]:
                return True
        else:
            return False
    def updateById(self):
        jsonData = self.getIO()
        newJsonData=[]
        for i in jsonData:
            if i['id']==self.student['id']:
                newJsonData.append(self.student)
                continue
            newJsonData.append(i)
        self.set(jsonData=newJsonData)
    def selectById(self):
        jsonData = self.getIO()
        newJsonData=None
        for i in jsonData:
            if i['id']==self.student.id:
                newJsonData=i
                break
        return newJsonData
    def deleteById(self):
        jsonData = self.getIO()
        newJsonData = []
        for i in jsonData:
            if i['id'] == self.student.id:
                continue
            newJsonData.append(i)
        self.set(newJsonData)

    def insertById(self):
        if self.judgeRepeat():
            print("已经存在相同身份证号码的学生信息！")
            return False
        self.student["id"] = self.getMaxId()
        jsonData = self.getIO()
        jsonData.append(self.student)
        return self.set(jsonData=jsonData)
        pass
class main:
    io=None
    def __init__(self):
        self.io = AllStudentIO()
        pass
    def chooseMode(self):
        print("*" * 30 + "欢迎来到九江学院学生信息管理系统" + "*" * 30)
        print("操作： 1.查看学生信息       2.删除学生的信息        3.插入学生的信息         4.修改学生的信息      5.退出登录")
        order = input("请输入你的指令:")
        while not re.match(r'[1-5]', order) or len(order) == 0 or len(order) > 1:
            order = input(f"{order}值格式错误，请重新输入你的指令:")
        if order == "1":
            self.selectAllStudent()
            pass
        if order == "2":
            self.selectAllStudent()
            self.deleteStudentById()
            self.selectAllStudent()
            pass
        if order == "3":
            flag=self.insertStudent()
            while flag:
                flag=self.insertStudent()
            pass
        if order == "4":
            self.selectAllStudent()
            self.updateStudentById()
            self.selectAllStudent()
            pass
        if order == "5":
            print("退出成功！")
            return False
        return True
    def selectAllStudent(self):
        print("*" * 20 +"查看学生信息子模块"+ "*" * 20)
        print("查询中....")
        data=self.io.getIO()
        print("序号       姓名       年龄       班级         学号           地址                   添加时间")
        for i in data:
            print(str(i['id'])+"         "+i['name']+"        "+i['age']+"         "+i["class_grade"]+"             "+i['id_card']\
                  +"               "+i['address']+"           "+i['time'])
        pass

    def insertStudent(self):
        print("*" * 20 + "学生信息添加子模块" + "*" * 20)
        name = input("请输入学生的姓名:")
        age=input("请输入学生的年龄:")
        while not re.match(r'[0-9]', age) or len(age) == 0:
            age = input(f"{age}值格式有误，请重新输入学生的年龄：")
        class_grade=input("请输入学生的年级:")
        id_card=input("请输入学生的学号:")
        while not re.match(r'[0-9]', id_card) or len(id_card) == 0 :
            id_card = input(f"{id_card}值格式有误，请重新输入学号：")
        address=input("请输入学生的家庭地址信息：")
        times = time.strftime('%Y{y}%m{m}%d{d} %H{h}%M{f}%S{s}').format(y='年', m='月', d='日', h='时', f='分', s='秒')

        student = Student(name=name,age=age,class_grade=class_grade,id_card=id_card,address=address,time=times)
        self.io.student=student.__dict__
        if self.io.insertById():
            print("添加信息成功")
        else:
            print("添加信息失败")
        isAgain = input("添加信息?y/n")
        while not re.match(r'^[yYnN]*$', isAgain) or len(isAgain) == 0 or len(isAgain) > 1:
            isAgain = input(f"{isAgain}值非法，是否继续添加信息?y/n")
        if isAgain == "y" or isAgain == "Y":
            return True
        else:
            return False

    def deleteStudentById(self):
        age = input("请输入要删除学生信息的序号:")
        while not re.match(r'[0-9]', age) or len(age) == 0:
            age = input(f"{age}值格式有误，请重新输入要删除学生信息的序号:")
        student =Student()
        student.id=int(age)
        self.io.student=student
        if self.io.selectById()!=None:
            self.io.deleteById()
            print("删除成功！")
        else:
            print("删除失败，找不到该序号的信息")

    def updateStudentById(self):
        age = input("请输入要更新学生信息的序号:")
        while not re.match(r'[0-9]', age) or len(age) == 0:
            age = input(f"{age}值格式有误，请重新输入要更新学生信息的序号:")
        student = Student()
        student.id = int(age)
        self.io.student = student
        selectResult=self.io.selectById()
        if  selectResult!= None:
            print(f"学生姓名为:{selectResult['name']}")
            name = input("请更新学生的姓名:")
            print(f"学生年龄为:{selectResult['age']}")
            age = input("请输入学生的年龄:")
            while not re.match(r'[0-9]', age) or len(age) == 0:
                age = input(f"{age}值格式有误，请重新输入学生的年龄：")
            print(f"学生班级为:{selectResult['class_grade']}")
            class_grade = input("请输入学生的年级:")
            print(f"学生学号为:{selectResult['id_card']}")
            id_card = input("请输入学生的学号:")
            while not re.match(r'[0-9]', id_card) or len(id_card) == 0:
                id_card = input(f"{id_card}值格式有误，请重新输入学号：")
            print(f"学生家庭地址信息为:{selectResult['address']}")
            address = input("请输入学生的家庭地址信息：")
            times = time.strftime('%Y{y}%m{m}%d{d} %H{h}%M{f}%S{s}').format(y='年', m='月', d='日', h='时', f='分', s='秒')

            student = Student(id=selectResult['id'],name=name, age=age, class_grade=class_grade, id_card=id_card, address=address, time=times)
            self.io.student = student.__dict__
            self.io.updateById()
            print("更新信息成功")
        else:
            print("更新信息失败，找不到该序号的信息！")
        pass


start=main()
while start.chooseMode():
    start.chooseMode()