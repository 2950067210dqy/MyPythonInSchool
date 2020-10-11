import re
import tkinter
import os
from tkinter import ttk
class curdWordsGui:
    top=None
    # 左边菜单栏的各个菜单名
    leftMenusStr=["单词导入","文章导入","网址导入","查看单词库"]
    # 底部单选框的变量值
    bottomMenvRBV=None
    # 提示信息的变量值
    tipMessageStr=None
    # 控制是否使用数据库存储
    isConnectDataBase=False
    # 控制是否使用文本存储
    isText=True
    def __init__(self):
        self.createGUI()

    # 返回主界面函数
    def backMainGui(self):
        self.destory()
        from GuessWords.GuessWordsClass.MainGui import mainGui
        GUI=mainGui()

    # 猜单词游戏按钮关联函数
    def guessWords(self):
        self.destory()
        pass

    # 创建python GUI
    def createGUI(self):
        self.top = tkinter.Tk()
        # 设置窗口的大小
        self.top.wm_geometry("700x550+500+100")
        # 设置不允许改变窗口的高宽
        self.top.wm_resizable(False, False)
        # 设置窗口标题
        self.top.title('词库操作')
        self.createSubGroup()
        self.top.mainloop()

    #   创建GUI当中的组件
    def createSubGroup(self):
        frame = tkinter.Frame(self.top).pack(fill="both")
        topMenuFrame=tkinter.Frame(frame)
        # 标题
        tkinter.Label(topMenuFrame,font=('楷体',22,'bold'),bd=5,text="单词操作",relief=tkinter.RAISED).pack(fill="x")
        tkinter.Button(topMenuFrame,text="返回",command=self.backMainGui).pack(side="right")
        topMenuFrame.pack(fill="x",side=tkinter.TOP)

        bottomMenuFrame = tkinter.Frame(frame)
        self.bottomMenvRBV = tkinter.IntVar()
        self.bottomMenvRBV.set(1)
        tkinter.Radiobutton(bottomMenuFrame, text="使用文本文件存储", variable=self.bottomMenvRBV, value=1, font=("宋体", 10),
                            command=self.changeIsText).pack(side="left")
        tkinter.Radiobutton(bottomMenuFrame, text="使用数据库连接", variable=self.bottomMenvRBV, value=2, font=("宋体", 10),
                            command=self.changeIsConnectDataBase).pack(side="left")
        self.tipMessageStr = tkinter.StringVar()
        tkinter.Label(bottomMenuFrame, textvariable=self.tipMessageStr, font=('楷体', 10, "bold"), fg="red").pack(
            side="right")
        bottomMenuFrame.pack(fill="x", side=tkinter.BOTTOM)



        # # 左边菜单项
        # leftMenuLB=tkinter.Listbox(frame,width=10,relief=tkinter.RAISED,bd=3,font=('黑体',15,'italic'),
        #                         selectbackground="black",selectborderwidth=10)
        # # 将数据添加到listBox中
        # self.insertIntoListBox(leftMenuLB, self.leftMenusStr)
        # # 默认选择第一项
        # leftMenuLB.selection_set(0)
        # # 菜单项添加监听事件
        # # //为什么不用鼠标单击事件<Button-1> 因为鼠标单击之后listbox的select不是立即发生的，
        # #   所以会造成点击之后，listbox的select的下标还停留在点击之前的select的下标
        # leftMenuLB.bind("<<ListboxSelect>>",self.bindHandlerAdaptor(fun=self.listBoxOnSelect,listbox=leftMenuLB))
        # leftMenuLB.pack(side=tkinter.LEFT,fill="y")
        #
        # rightFrame=tkinter.Frame(frame)
        # tkinter.Label(rightFrame,font=('黑体',13),text="请输入您要导入的单词,用空格隔开").pack()
        # wordsText=tkinter.Text(rightFrame,width=40,height=15,font=('楷体',17),selectbackground="red")
        # wordsText.pack()
        # buttonFrame=tkinter.Frame(rightFrame)
        # tkinter.Button(buttonFrame,text="确定导入",command=self.commandHandlerAdapator(fun=self.importToWords,Text=wordsText)).pack(side="left",padx=20)
        # tkinter.Button(buttonFrame, text="清空单词",command=self.commandHandlerAdapator(fun=self.cleanText,Text=wordsText)).pack(side="right")
        # buttonFrame.pack()
        # rightFrame.pack()
        tab = ttk.Notebook(frame)

        rightFrame1 = tkinter.Frame(tab)
        tkinter.Label(rightFrame1, font=('黑体', 13), text="请输入您要导入的单词,用空格隔开").pack()
        wordsText = tkinter.Text(rightFrame1, width=40, height=15, font=('楷体', 17), selectbackground="red")
        wordsText.pack()
        buttonFrame = tkinter.Frame(rightFrame1)
        tkinter.Button(buttonFrame, text="确定导入",
                       command=self.commandHandlerAdapator(fun=self.importToWords, Text=wordsText)).pack(side="left",
                                                                                                         padx=20)
        tkinter.Button(buttonFrame, text="清空单词",
                       command=self.commandHandlerAdapator(fun=self.cleanText, Text=wordsText)).pack(side="right")
        buttonFrame.pack()
        tab1=tab.add(rightFrame1,text=self.leftMenusStr[0])

        rightFrame2 = tkinter.Frame(tab)

        tab2 = tab.add(rightFrame2, text=self.leftMenusStr[1])
        tab.pack(side=tkinter.TOP)




    # 将单词导入词库函数操作
    def importToWords(self,Text):
        # 获取文本
        strs=Text.get("1.0",tkinter.END)
        # 清空输入框
        self.cleanText(Text)
        # 拆分
        strlist=strs.split(" ")
        # 过滤
        result = filter(lambda x:re.findall(r'[A-Za-z]',x), strlist)


        if self.isText:
            with open(os.getcwd()+'\\TXT\\words.txt', 'a+') as fp:
                for item in result:
                    print(item+"1")
                    fp.write(item + '\n')
            fp.close()
            self.InsertTipMessage("添加成功")
        if self.isConnectDataBase:
            pass
    # 清空输入栏
    def cleanText(self,Text):
        Text.delete("1.0",tkinter.END)
        self.InsertTipMessage("输入框清空完成")
    # 底部菜单的radiobutton的 使用文本文件存储 监听函数
    def changeIsText(self):
        self.isConnectDataBase = False
        self.isText=True
        self.InsertTipMessage("isConnectDataBase:" + str(self.isConnectDataBase) + "\nisText:" + str(self.isText))
    # 底部菜单的radiobutton的 使使用数据库连接 监听函数
    def changeIsConnectDataBase(self):
        self.isText=False
        self.isConnectDataBase=True
        self.InsertTipMessage("isConnectDataBase:" + str(self.isConnectDataBase) + "\nisText:" + str(self.isText))

    # bind方法的监听函数的中间函数（为了传递其他参数）
    def bindHandlerAdaptor(self, fun, **eles):
        return lambda event, eles=eles: fun(event, **eles)
    # command的监听函数的中间函数（为了传递其他参数）
    def commandHandlerAdapator(self, fun, **eles):
        return lambda eles=eles: fun(**eles)
    # #  listBox的select发生改变的监听函数
    # def listBoxOnSelect(self,event,listbox):
    #     # 根据选中的第几项菜单显示什么功能
    #     try:
    #         index=int(listbox.curselection()[0])
    #         if index==0:
    #             self.InsertTipMessage(index)
    #             pass
    #         elif index==1:
    #             self.InsertTipMessage(index)
    #             pass
    #         elif index==2:
    #             self.InsertTipMessage(index)
    #             pass
    #         elif index==3:
    #             self.InsertTipMessage(index)
    #             pass
    #     except Exception:
    #         pass

    #  将数据插入到ListBox中
    def insertIntoListBox(self,listBox,strs=[]):
        for i in strs:
            listBox.insert("end",i)
    #销毁GUI
    def destory(self):
        # 关闭当前窗口
        self.top.destroy()
    # 添加提示信息
    def InsertTipMessage(self,msg):
        self.tipMessageStr.set(str(msg))


