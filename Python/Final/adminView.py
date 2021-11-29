import os

userFile = "userList.txt"

class adminView:
    def __init__(self, _name=str, _pwd=str):

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
                print("管理员退出成功")
            elif option == 1:
                self.viewAllUser()
            elif option == 2:
                self.addExp()




    def menu(self):
        # 输出菜单
        print('''    │   =======管理员菜单========│
    │   1 查看所有用户                                     
    │   2 快递操作               │ 
    │   0 退出登录               │
    │   =======管理员菜单========│''')
    def viewAllUser(self):

            user_new = []
            if os.path.exists(userFile):
                with open(userFile, 'r') as rfile:
                    user_old = rfile.readlines()
                for list in user_old:
                    user_new.append(eval(list))
                if user_new:
                    self.show_user(user_new)

    def show_user(self,userList):

        if not userList:
            print("(o@.@o) 无数据信息 (o@.@o) \n")
            return

        print("ID", "用户名", "密码", "待取包裹")

        for user in userList:
            print(
                (user.get("id"), str(user.get("username")), str(user.get("password")), user.get("expNum"))
                                   )

    def addExp(self):
        self.viewAllUser()
        id = int(input("请输入摇操作的ID："))
        if os.path.exists(userFile):
            with open(userFile, 'r') as rfile:
                user_old = rfile.readlines()
        else:
            return

        with open(userFile, "w") as wfile:
            for user in user_old:
                d = dict(eval(user))
                if d["id"] == id:
                    print("当前位置：{0}  快递个数：{1} ".format(d['id'], d['expNum'],))

                    while True:
                        try:
                            d["expNum"] = input("输入快递个数：")


                        except:
                            print("您的输入有误，请重新输入。")
                        else:
                            break
                    user = str(d)
                    wfile.write(user + "\n")
                    print("修改成功！")
                else:
                    wfile.write(user)


