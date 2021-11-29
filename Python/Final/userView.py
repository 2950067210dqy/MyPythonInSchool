import os

userFile = "userList.txt"  # 定义保存学生信息的文件名

class UserView:
    def __init__(self, _id=int, _name=str, _pwd=str):
        self._id = _id
        self.name = _name
        self.pwd = _pwd
        self.main()



    def choose(self):
        data = input("请选择：")
        try:
            inputData = eval(data)
            if type(inputData) == int:
                # break
                if inputData in range(0, 4):
                    return inputData

        except:
            pass

    def main(self):

        global start

        start = True
        while (start):
            self.menu()
            option = self.choose()

            if option == 0:

                start = False
            elif option == 1:
                self.viewInfo(self._id,self.name,self.pwd)
            elif option == 2:
                self.updateInfo(self._id,self.name,self.pwd)
            elif option == 3:
                self.viewExp(self._id)
            elif option == 4:

                self.dropId(self._id)
                start = False
                print('已退出！')
            elif option == 5:

                self.dropId(id)


    def menu(self):
        # 输出菜单
        print('''    │   =========用户菜单==========│
    │   1 查看信息                                     
    │   2 修改信息                 │ 
    │   3 查看快递                 │
    │   4 注销账号                 │
    │   0 退出登录                 │
    │   =========用户菜单==========│ ''')
    def viewInfo(self,id,username,password):
        if os.path.exists(userFile):
            with open(userFile, 'r') as rfile:
                user_old = rfile.readlines()
        else:
            return

        with open(userFile, 'r') as file:

            for list in user_old:
                d = dict(eval(list))  # 字符串转字典
                if d['id'] == id:
                        print("序号：{0} 用户名：{1} 密码：{2}".format(d['id'], d['username'],d['password']))
    def updateInfo(self,id,username,password):

        if os.path.exists(userFile):
            with open(userFile, 'r') as rfile:
                user_old = rfile.readlines()
        else:
            return

        with open(userFile, "w") as wfile:
            for user in user_old:
                d = dict(eval(user))
                if d["username"] == username:
                    print("你当前的用户名为：",username)
                    while True:
                        try:
                            d["username"] = input("new username：")
                            d["password"] = input("new password：")

                        except:
                            print("您的输入有误，请重新输入。")
                        else:
                            break
                    user = str(d)
                    wfile.write(user + "\n")
                    print("修改成功！")
                else:
                    wfile.write(user)

    def dropId(self,id):
        print(id)

        mark = True
        while mark:

            if    id is not "":
                if os.path.exists(userFile):
                    with open(userFile, 'r') as rfile:
                        user_old = rfile.readlines()
                else:
                    user_old = []
                ifdel = False
                if user_old:
                    with open(userFile, 'w') as wfile:
                        d = {}
                        for list in user_old:
                            d = dict(eval(list))
                            if d['id'] !=id:
                                wfile.write(str(d) + "\n")
                            else:
                                ifdel = True
                        if ifdel:
                            print("ID为 %s 的账号信息已经被删除..." % id)
                            mark=False

                else:
                    print("无学生信息...")
                    break
    def viewExp(self,id):
        if os.path.exists(userFile):
            with open(userFile, 'r') as rfile:
                user_old = rfile.readlines()
        else:
            return

        with open(userFile, 'r') as file:

            for list in user_old:
                d = dict(eval(list))
                if d['id'] == id:
                    print("尊敬的：{0}用户 ，您有 {1} 个快递包裹待领取".format( d['username'], d['expNum']))