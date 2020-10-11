import tkinter
from GuessWords.GuessWordsClass.CurdDataBaseAdptorByGuessWords import curdDataBaseAdptorByGuessWords
import os
import re
import tkinter.messagebox
from tkinter import ttk
class guessWordsGui:
    top=None
    # 底部单选框的变量值
    bottomMenvRBV = None
    # 提示信息的变量值
    tipMessageStr = None
    # 控制是否使用数据库存储
    isConnectDataBase = False
    # 控制是否使用文本存储
    isText = True
    # 连接的数据库
    db = None
    # 连接的数据库的游标
    cursor = None
    def __init__(self):
        self.createGUI()
    # 单词操作按钮关联函数
    def curdWords(self):
        self.destory()
        pass

    # 猜单词游戏按钮关联函数
    def guessWords(self):
        self.destory()
        pass

    # 创建python GUI
    def createGUI(self):
        self.top = tkinter.Tk()
        # 设置窗口的大小
        self.top.wm_geometry("500x500+600+100")
        # 设置不允许改变窗口的高宽
        self.top.wm_resizable(False, False)
        # 设置窗口标题
        self.top.title('猜单词游戏')
        self.createSubGroup()
        self.top.mainloop()

    #   创建GUI当中的组件
    def createSubGroup(self):
        frame = tkinter.Frame(self.top).pack(fill="both")
        bottomMenuFrame = tkinter.Frame(frame)
        self.bottomMenvRBV = tkinter.IntVar()
        if self.isText:
            self.bottomMenvRBV.set(1)
        if self.isConnectDataBase:
            self.bottomMenvRBV.set(2)
        tkinter.Radiobutton(bottomMenuFrame, text="使用文本文件存储", variable=self.bottomMenvRBV, value=1, font=("宋体", 10),
                            command=self.changeIsText).pack(side="left")
        tkinter.Radiobutton(bottomMenuFrame, text="使用数据库连接", variable=self.bottomMenvRBV, value=2, font=("宋体", 10),
                            command=self.changeIsConnectDataBase).pack(side="left")
        self.tipMessageStr = tkinter.StringVar()
        tkinter.Label(bottomMenuFrame, textvariable=self.tipMessageStr, font=('楷体', 10, "bold"), fg="red").pack(
            side="right")
        bottomMenuFrame.pack(fill="x", side=tkinter.BOTTOM)

    #销毁GUI
    def destory(self):
        # 关闭当前窗口
        self.top.destroy()

    # 底部菜单的radiobutton的 使用文本文件存储 监听函数
    def changeIsText(self):
        self.isConnectDataBase = False
        self.isText = True
        curdDB = curdDataBaseAdptorByGuessWords()
        # 关闭数据库
        if self.db:
            try:
                curdDB.close(self.db)
            except Exception:
                pass
        self.InsertTipMessage("切换文本存储成功")

    # 底部菜单的radiobutton的 使使用数据库连接 监听函数
    def changeIsConnectDataBase(self):
        self.isText = False
        self.isConnectDataBase = True
        # 连接数据库
        curdDB = curdDataBaseAdptorByGuessWords()
        self.db = curdDB.connectDataBase()
        self.cursor = curdDB.getCursor(self.db)
        self.InsertTipMessage("切换数据库成功")

    # bind方法的监听函数的中间函数（为了传递其他参数）
    def bindHandlerAdaptor(self, fun, **eles):
        return lambda event, eles=eles: fun(event, **eles)

    # command的监听函数的中间函数（为了传递其他参数）
    def commandHandlerAdapator(self, fun, **eles):
        return lambda eles=eles: fun(**eles)
    # 添加提示信息
    def InsertTipMessage(self,msg):
        self.tipMessageStr.set(str(msg))

