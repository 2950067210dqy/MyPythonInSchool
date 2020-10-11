import tkinter
from GuessWords.GuessWordsClass.CurdDataBaseAdptorByGuessWords import curdDataBaseAdptorByGuessWords
import os
import re
import tkinter.messagebox
import random
from tkinter import ttk
class guessWordsGui:
    top = None
    #输入框
    entry=None
    #按钮
    okBt=None
    nextBt=None
    tipBt=None

    # 底部单选框的变量值
    bottomMenvRBV = None
    # 提示信息的变量值
    tipMessageStr = None
    # 控制是否使用数据库存储
    isConnectDataBase = None
    # 控制是否使用文本存储
    isText = None
    # 连接的数据库
    db = None
    # 连接的数据库的游标
    cursor = None
    # 控制关卡数
    pack=None
    packNum=1
    #控制每关的题数
    num=0
    # 所有的单词
    words=[]
    # 一共关卡
    allpacks=None
    # 显示乱序的单词
    sdrow=None
    sdrowNum=""
    # 存储不乱序的单词
    word=None
    wordNum=""
    # 每关的题目数量
    packOfNums=10
    def __init__(self,bottomMenvRBVNum):
        self.words=[]
        self.createSaveBaseFlag(bottomMenvRBVNum)
        self.getWords()
        self.allpacks=int(len(self.words))//self.packOfNums
        self.createGUI(bottomMenvRBVNum)

    # 根据传过来的值来确定存储对象
    def createSaveBaseFlag(self,bottomMenvRBVNum):
        if bottomMenvRBVNum==1:
            self.isText=True
            self.isConnectDataBase=False
        else:
            #连接数据库
            curdDB = curdDataBaseAdptorByGuessWords()
            self.db = curdDB.connectDataBase()
            self.cursor = curdDB.getCursor(self.db)
            self.isText = False
            self.isConnectDataBase = True
    # 创建python GUI
    def createGUI(self,bottomMenvRBVNum):
        self.top = tkinter.Tk()
        # 设置窗口的大小
        self.top.wm_geometry("500x180+600+100")
        # 设置不允许改变窗口的高宽
        self.top.wm_resizable(False, False)
        # 设置窗口标题
        self.top.title('猜单词游戏')
        self.createSubGroup(bottomMenvRBVNum)
        self.top.mainloop()

    #   创建GUI当中的组件
    def createSubGroup(self,bottomMenvRBVNum):
        self.pack = tkinter.StringVar()
        self.pack.set(str(self.packNum))
        self.sdrowNum=self.LuanXu(self.words[(self.packNum-1)*self.packOfNums:self.packNum*self.packOfNums][self.num])
        self.sdrow = tkinter.StringVar()
        self.sdrow.set(self.sdrowNum)
        self.wordNum=self.words[(self.packNum-1)*self.packOfNums:self.packNum*self.packOfNums][self.num]
        self.word = tkinter.StringVar()
        self.word.set(self.wordNum)

        frame = tkinter.Frame(self.top).pack(fill="both")
        topFrame=tkinter.Frame(frame)
        tkinter.Label(topFrame,text="第",fg="red",font=("宋体",25,"bold")).pack(side="left")
        tkinter.Label(topFrame,  textvariable=self.pack, fg="red", font=("宋体", 25, "bold")).pack(side="left")
        tkinter.Label(topFrame, text="关", fg="red", font=("宋体", 25, "bold")).pack(side="left")
        topFrame.pack(fill="x", side=tkinter.TOP)


        bottomMenuFrame = tkinter.Frame(frame)
        self.bottomMenvRBV = tkinter.IntVar()
        if self.isText:
            self.bottomMenvRBV.set(bottomMenvRBVNum)
        if self.isConnectDataBase:
            self.bottomMenvRBV.set(bottomMenvRBVNum)
        tkinter.Radiobutton(bottomMenuFrame, text="使用文本文件存储", variable=self.bottomMenvRBV, value=1, font=("宋体", 10),
                            command=self.changeIsText,indicatoron=0,state="disabled").pack(side="left")
        tkinter.Radiobutton(bottomMenuFrame, text="使用数据库连接", variable=self.bottomMenvRBV, value=2, font=("宋体", 10),
                            command=self.changeIsConnectDataBase,indicatoron=0,state="disabled").pack(side="left")
        tkinter.Button(bottomMenuFrame,text="返回",command=self.backMainGui,font=("宋体", 10),width=10).pack(side="left")
        self.tipMessageStr = tkinter.StringVar()
        tkinter.Label(bottomMenuFrame, textvariable=self.tipMessageStr, font=('楷体', 10, "bold"), fg="red").pack(
            side="right")
        bottomMenuFrame.pack(fill="x", side=tkinter.BOTTOM)


        centerFrame=tkinter.Frame(frame)

        LuanXuFrame=tkinter.Frame(centerFrame)
        tkinter.Label(LuanXuFrame,text="乱序的单词:",widt=15,font=('黑体',15)).pack(side="left")
        tkinter.Label(LuanXuFrame,textvariable=self.sdrow,widt=15,font=('黑体',25),bg="black",fg="white").pack(side="left")
        LuanXuFrame.pack(fill="x")

        entryFrame=tkinter.Frame(centerFrame)
        tkinter.Label(entryFrame,text="请输入单词:",widt=15,font=('黑体',15)).pack(side="left")
        self.entry=tkinter.Entry(entryFrame,widt=15,font=('黑体',25))
        self.entry.pack(side="left")
        entryFrame.pack(fill="x")

        buttonFrame=tkinter.Frame(centerFrame)
        self.okBt=tkinter.Button(buttonFrame,text="确定答案",widt=15,font=('黑体',15),command=self.commandHandlerAdapator(self.OKAnswer))
        self.okBt.pack(side="left",padx=10)
        self.nextBt = tkinter.Button(buttonFrame, text="下一题", widt=15, font=('黑体', 15),command=self.commandHandlerAdapator(self.nextPack),state="disabled")
        self.nextBt.pack(side="left",padx=10)
        self.tipBt=tkinter.Button(buttonFrame,text="提示",widt=15,font=('黑体',15),command=self.commandHandlerAdapator(self.tipHandle),state="disabled")
        self.tipBt.pack(side="left",padx=10)
        buttonFrame.pack(fill="x")

        centerFrame.pack(fill="x",side=tkinter.TOP)
    # 确定答案按钮事件
    def OKAnswer(self):
        if self.wordNum==str(self.entry.get()):
            self.InsertTipMessage("恭喜你猜对了")
            self.okBt['state']='disabled'
            self.nextBt['state']='normal'
        else:
            self.InsertTipMessage("猜错了呢，继续加油！")
            self.tipBt['state']='normal'
    # 下一题按钮事件
    def nextPack(self):
        if self.packNum==self.allpacks:
            tkinter.messagebox.askquestion("通关", "题库没题目了，您真厉害！\n导入单词之后再来猜单词吧，您已经猜了" + str(len(self.words))+"个单词")
        self.num=self.num+1
        if self.num>self.packOfNums-1:
            self.num=0
            self.packNum=self.packNum+1
            self.pack.set(str(self.packNum))
        self.sdrowNum = self.LuanXu(self.words[(self.packNum - 1) * self.packOfNums :self.packNum * self.packOfNums][self.num])
        self.sdrow.set(self.sdrowNum)
        self.wordNum = self.words[(self.packNum - 1) * self.packOfNums :self.packNum * self.packOfNums][self.num]
        self.word.set(self.wordNum)
        self.okBt['state'] = 'normal'
        self.nextBt['state'] = 'disabled'
        self.tipBt['state']='disabled'
    # 提示按钮事件
    def tipHandle(self):
        tkinter.messagebox.askquestion("提示","单词的正确排序为:"+self.wordNum)
    # 单词乱序功能
    def LuanXu(self,word):
        Lword = ""
        while word:  # word 不是空串循环
            # 根据 word 长度产生 word 的随机位置
            position = random.randrange(len(word))
            # 将 position 位置的字母组合到乱序后单词
            Lword += word[position]
            # 通过切片将 position 位置的字母从原单词中删除
            word = word[:position] + word[(position + 1):]
        return Lword
    # 读取单词的操作
    def getWords(self):
        if self.isText:
            words = self.getWordsByTXT()
            self.words=words
        if self.isConnectDataBase:
            words = self.getWordsByDB()
            for i in range(0,len(words)):
                self.words.append(words[i][1])
    # 从文本取出单词 列表形式存储
    def getWordsByTXT(self):
        with open(os.getcwd() + '\\TXT\\words.txt', 'r') as fp:
            # 读取所有行
            words = fp.readlines()
            words = self.StrSplitOfList(oldList=words, string="\n")
        fp.close()
        return words
    # 从数据库取出单词 二维元组存储
    def getWordsByDB(self):
        curdDB = curdDataBaseAdptorByGuessWords()
        try:
            curdDB.selectAll(cursor=self.cursor)
            wordsByDB=self.cursor.fetchall()
        except Exception:
            curdDB.rollback(self.db)
        curdDB.commit(self.db)
        return wordsByDB

    #销毁GUI
    def destory(self):
        # 关闭当前窗口
        if self.db:
            curdDB = curdDataBaseAdptorByGuessWords()
            try:
                curdDB.close(self.db)
            except Exception:
                pass
        self.words = []
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
    # 返回主界面函数
    def backMainGui(self):
        self.destory()
        from GuessWords.GuessWordsClass.MainGui import mainGui
        mainGui()
 #  将列表中的字符串切片
    def StrSplitOfList(self,oldList, string):
        newList = []
        for i in oldList:
            newList.append(str(i).split(string)[0])
        return newList
    # 添加提示信息
    def InsertTipMessage(self,msg):
        self.tipMessageStr.set(str(msg))
