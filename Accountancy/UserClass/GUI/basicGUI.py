import re
import tkinter
import tkinter.messagebox
import os
from tkinter import ttk
from Accountancy.UserClass.Util.Setting import Setting
from Accountancy.UserClass.Reptile.reptile import reptile
class basicGUI():
    top=None

    # 底部单选框的变量值
    bottomMenvRBV=None
    # 提示信息的变量值
    tipMessageStr=None
    # 控制是否使用数据库存储
    isConnectDataBase=False
    # 控制是否使用文本存储
    isText=True
    # 连接的数据库
    db=None
    # 连接的数据库的游标
    cursor=None
    # 展现单词库的表格
    table=None
    # 保存每个单词所在的表格index
    table_tags=[]
    def __init__(self):
        setting=Setting()
        self.option=setting.getGUISetting()
        self.createGUI()

    # 返回主界面函数
    def backMainGui(self):
        self.destory()
        from GuessWords.GuessWordsClass.MainGui import mainGui
        mainGui()

    # 猜单词游戏按钮关联函数
    def guessWords(self):
        self.destory()
        pass

    # 创建python GUI
    def createGUI(self):
        self.top = tkinter.Tk()
        # 设置窗口的大小
        self.top.wm_geometry(self.option['width']+'x'+self.option['height']+'+'+self.option['left']+'+'+self.option['top'])#"800x550+500+100"
        # 设置不允许改变窗口的高宽
        self.top.wm_resizable(False, False)
        # 设置窗口标题
        self.top.title(self.option['title'])
        self.createSubGroup()
        self.top.mainloop()

    #   创建GUI当中的组件
    def createSubGroup(self):
        frame = tkinter.Frame(self.top).pack(fill="both")
        topMenuFrame=tkinter.Frame(frame)
        # 标题
        tkinter.Label(topMenuFrame,font=('楷体',22,'bold'),bd=5,text=self.option['labeltitle'],relief=tkinter.RAISED).pack(fill="x")
        topMenuFrame.pack(fill="x",side=tkinter.TOP)

        bottomMenuFrame = tkinter.Frame(frame)
        self.tipMessageStr = tkinter.StringVar()
        tkinter.Label(bottomMenuFrame, textvariable=self.tipMessageStr, font=('楷体', 10, "bold"), fg="red").pack(
            side="left")
        bottomMenuFrame.pack(fill="x", side=tkinter.BOTTOM)




        tab = ttk.Notebook(frame)
        #第一个菜单页面
        rightFrame1 = tkinter.Frame(tab)
        tkinter.Label(rightFrame1, font=('黑体', 13), text=self.option['tip1']).pack()
        wordsText = tkinter.Text(rightFrame1, width=64, height=15, font=('楷体', 17), selectbackground="red")
        wordsTextSb=tkinter.Scrollbar()
        wordsTextSb.pack(side=tkinter.RIGHT, fill=tkinter.Y)
        # 两个控件关联
        wordsTextSb.config(command=wordsText.yview)
        wordsText.config(yscrollcommand=wordsTextSb.set)
        wordsText.pack()
        buttonFrame = tkinter.Frame(rightFrame1)
        tkinter.Button(buttonFrame, text=self.option['btnlabel1'],
                       command=self.commandHandlerAdapator(fun=self.importToWords, Text=wordsText)).pack(side="left",
                                                                                                         padx=20)
        tkinter.Button(buttonFrame, text=self.option['btnlabel2'],
                       command=self.commandHandlerAdapator(fun=self.cleanText, Text=wordsText)).pack(side="right")
        buttonFrame.pack()
        tab1=tab.add(rightFrame1,text=self.option['menulabel1'])


        # 第二个菜单页面
        rightFrame2 = tkinter.Frame(tab)
        tkinter.Label(rightFrame2, font=('黑体', 13), text=self.option['tip2']).pack()
        wordsText2 = tkinter.Text(rightFrame2, width=64, height=15, font=('楷体', 17), selectbackground="red")
        # 两个控件关联
        wordsTextSb.config(command=wordsText2.yview)
        wordsText2.config(yscrollcommand=wordsTextSb.set)
        wordsText2.pack()
        buttonFrame2 = tkinter.Frame(rightFrame2)
        tkinter.Button(buttonFrame2, text=self.option['btnlabel1'],
                       command=self.commandHandlerAdapator(fun=self.importToWords, Text=wordsText2,type="essay")).pack(side="left",
                                                                                                         padx=20)
        tkinter.Button(buttonFrame2, text=self.option['btnlabel2'],
                       command=self.commandHandlerAdapator(fun=self.cleanText, Text=wordsText2)).pack(side="right")
        buttonFrame2.pack()
        tab2 = tab.add(rightFrame2, text=self.option['menulabel2'])



        # 第三个菜单页面
        rightFrame3 = tkinter.Frame(tab)
        tkinter.Label(rightFrame3, font=('黑体', 13), text=self.option['tip3']).pack()
        wordsText3 = tkinter.Text(rightFrame3, width=64, height=15, font=('楷体', 17), selectbackground="red")
        # 两个控件关联
        wordsTextSb.config(command=wordsText3.yview)
        wordsText3.config(yscrollcommand=wordsTextSb.set)
        wordsText3.pack()
        buttonFrame3 = tkinter.Frame(rightFrame3)
        tkinter.Button(buttonFrame3,text=self.option['btnlabel1'],
                       command=self.commandHandlerAdapator(fun=self.importToWords, Text=wordsText3, type="url")).pack(
            side="left",
            padx=20)
        tkinter.Button(buttonFrame3,text=self.option['btnlabel3'],
                       command=self.commandHandlerAdapator(fun=self.cleanText, Text=wordsText3)).pack(
            side="right")
        buttonFrame3.pack()
        tab3 = tab.add(rightFrame3, text=self.option['menulabel3'])


        # 四个菜单页面
        rightFrame4 = tkinter.Frame(tab)
        table_title = ["序号", "单词", "翻译", "保存时间", "删除"]
        table_title_id = [0, 1, 2, 3, 4]
        self.table=ttk.Treeview(rightFrame4,columns=table_title_id,show="headings",height=18)
        # 两个控件关联
        wordsTextSb.config(command=self.table.yview)
        self.table.config(yscrollcommand=wordsTextSb.set)
        for i in table_title_id:
            self.table.column(i,width=150,anchor='center')
            # 表格标题展现
            self.table.heading(i, text=table_title[i])
        #读取数据并放在上面
        self.tableShowWords()
        self.table.pack()
        delteWordsBT = tkinter.Button(rightFrame4, text="删除单词表",
                                      command=self.commandHandlerAdapator(self.deleteAllWords))
        delteWordsBT.pack(fill="x")
        tab4 = tab.add(rightFrame4, text=self.option['menulabel4'])
        tab.pack(side=tkinter.TOP,fill="x")
        tab.select(tab1)

    # 删除单词表操作
    def deleteAllWords(self):
            if self.isText:
                self.deleteWordsByTxt()
            if self.isConnectDataBase:
                self.deleteWordsByDB()
            self.tableHideWords()
    # 删除文本文件存储的单词表
    def deleteWordsByTxt(self):
        with open(os.getcwd() + '\\TXT\\words.txt', 'w') as fp:
            fp.write("")
        fp.close()
        self.InsertTipMessage("文本存储单词表删除成功")
    # 删除数据库文件的单词表
    def deleteWordsByDB(self):
        curdDB=curdDataBaseAdptorByGuessWords()
        try:
            self.InsertTipMessage("数据库单词表删除成功,共删除单词"+str(curdDB.deleteAll(self.cursor))+"个")
        except Exception:
            curdDB.rollback(self.db)
        curdDB.commit(self.db)
    # 读取单词并显示在表格上
    def tableShowWords(self):
        # if self.isText:
        #     words=self.getWordsByTXT()
        #     for i in words :
        #         # 向表格插入数据并保存index
        #         self.table_tags.append(self.table.insert("","end",values=("",i,"","","")))
        # if self.isConnectDataBase:
        #     words=self.getWordsByDB()
        #     # print(words)
        #     for i in words:
        #         self.table_tags.append(self.table.insert("", "end", values=(i[0], i[1], i[2], i[3], "")))
        pass
    # 将表格的显示所有单词删除
    def tableHideWords(self):
        for i in range(0,len(self.table_tags)):
            self.table.delete(self.table_tags[i])
        self.table_tags=[]
    # 将开始爬虫
    def importToWords(self,Text,type=""):
        # 获取文本
        strs=Text.get("1.0",tkinter.END)
        # 将两端换行符去除
        strs=strs.strip("\n")
        # 将两端空格去除
        strs=strs.strip()
        # 拆分
        strlist=strs.split(" ")

        if strlist[0]=='':
            self.InsertTipMessage("输入框不能为空!!!")
            return
        # 判断输入框输入的是不是url
        if type=="url":
            # 过滤掉不是url的字符串
            result = filter(lambda x:re.findall(r'^([hH][tT]{2}[pP]://|[hH][tT]{2}[pP][sS]://)(([A-Za-z0-9-~]+).)+([A-Za-z0-9-~\\/])+$',x),strlist)
        else:
            result=reptile().getWebSites(videoname=strlist)
        print(result)
        result=reptile(urlList=result).start()
        # # 过滤 过滤输入重复的 过滤其他字符 上面的过滤是粗过滤
        # result = self.fiterSS(result)
        # # 如果存储着相同的单词去除
        # result = self.fiterSaveSS(result)
        # # 去除单个字母组成的单词
        # result = filter(lambda x:len(x)>1,result)
        #根据选择的存储方式存储
        # if self.isText:
        #     self.importToTXT(fiter=result)
        # if self.isConnectDataBase:
        #     self.importToDataBase(fiter=result)
        # 清空输入框
        self.cleanText(Text)
    # 从文本取出单词 列表形式存储
    def getWordsByTXT(self):
        # with open(os.getcwd() + '\\TXT\\words.txt', 'r') as fp:
        #     # 读取所有行
        #     words = fp.readlines()
        #     words = self.StrSplitOfList(oldList=words, string="\n")
        # fp.close()
        # return words
        pass
    # 从数据库取出单词 二维元组存储
    def getWordsByDB(self):
        # curdDB = curdDataBaseAdptorByGuessWords()
        # try:
        #     curdDB.selectAll(cursor=self.cursor)
        #     wordsByDB=self.cursor.fetchall()
        # except Exception:
        #     curdDB.rollback(self.db)
        # curdDB.commit(self.db)
        # return wordsByDB
        pass
    #  将列表中的字符串切片
    def StrSplitOfList(self,oldList, string):
        newList = []
        for i in oldList:
            newList.append(str(i).split(string)[0])
        return newList
    # 过滤存储存在的单词
    def fiterSaveSS(self,result=None):
        if self.isText:
            saveWordsList=self.getWordsByTXT()
            return filter(lambda x:x not in saveWordsList,result)
        if self.isConnectDataBase:
            saveWordsTuple2=self.getWordsByDB()
            newWordsList=[]
            for i in saveWordsTuple2:
                newWordsList.append(i[1])
            print(newWordsList)
            return filter(lambda x:x not in newWordsList,result)
    # 过滤重复单词功能
    def fiterSS(self,result=None):
        newResult=[]
        for item in result:
            item=item.strip("\n")
            item=item.strip()
            item=re.sub(r"[^a-zA-Z]","",item)
            if item not in newResult :
                newResult.append(item)
        return newResult
    #将单词导入到文本文件函数
    def importToTXT(self,fiter):
        with open(os.getcwd() + '\\TXT\\words.txt', 'a+') as fp:
            i=0
            for item in fiter:
                fp.write(item + '\n')
                i=i+1
        fp.close()
        self.InsertTipMessage("添加成功,共添加"+str(i)+"个单词")
    #将单词导入到数据库函数
    def importToDataBase(self,fiter):

        curdDB=curdDataBaseAdptorByGuessWords()
        curdDB.createTable(self.cursor)
        try:
            i=0
            for item in fiter:
                self.InsertTipMessage(curdDB.insert(self.cursor,item))
                i = i + 1
            self.InsertTipMessage("添加成功,共添加"+str(i)+"个单词")
        except Exception :

            self.InsertTipMessage("添加失败")
            curdDB.rollback(self.db)
        curdDB.commit(self.db)

    # 清空输入栏
    def cleanText(self,Text):
        Text.delete("1.0",tkinter.END)
        self.InsertTipMessage("输入框清空完成")
    # 底部菜单的radiobutton的 使用文本文件存储 监听函数
    def changeIsText(self):
        self.isConnectDataBase = False
        self.isText=True
        curdDB = curdDataBaseAdptorByGuessWords()
        #关闭数据库
        if self.db:
            try:
                curdDB.close(self.db)
            except Exception:
                pass
        # 更改表格显示数据的来源
        self.tableHideWords()
        self.tableShowWords()
        self.InsertTipMessage("切换文本存储成功")
    # 底部菜单的radiobutton的 使使用数据库连接 监听函数
    def changeIsConnectDataBase(self):
        self.isText=False
        self.isConnectDataBase=True
        #连接数据库
        curdDB = curdDataBaseAdptorByGuessWords()

        self.db = curdDB.connectDataBase()
        if isinstance(self.db, str):
            self.InsertTipMessage(self.db)
            return
        self.cursor = curdDB.getCursor(self.db)
        # 更改表格显示数据的来源
        self.tableHideWords()
        self.tableShowWords()
        self.InsertTipMessage("切换数据库成功")
    # # bind方法的监听函数的中间函数（为了传递其他参数）
    # def bindHandlerAdaptor(self, fun, **eles):
    #     return lambda event, eles=eles: fun(event, **eles)
    # command的监听函数的中间函数（为了传递其他参数）
    def commandHandlerAdapator(self, fun, **eles):
        return lambda eles=eles: fun(**eles)
    #销毁GUI
    def destory(self):
        # 关闭当前窗口
        if self.db:
            curdDB = curdDataBaseAdptorByGuessWords()
            try:
                curdDB.close(self.db)
            except Exception:
                pass
        self.table_tags=[]
        print(self.table_tags)
        self.top.destroy()
    # 添加提示信息
    def InsertTipMessage(self,msg):
        self.tipMessageStr.set(str(msg))


