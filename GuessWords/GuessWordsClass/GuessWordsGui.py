import tkinter
class guessWordsGui:
    top=None
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
        self.top.wm_geometry("500x300+500+100")
        # 设置不允许改变窗口的高宽
        self.top.wm_resizable(False, False)
        # 设置窗口标题
        self.top.title('猜单词游戏')
        self.createSubGroup()
        self.top.mainloop()

    #   创建GUI当中的组件
    def createSubGroup(self):
        frame = tkinter.Frame(self.top).pack(fill="both")
        tkinter.Button(frame, text="单词操作", width=25, height=7, bd=3, bg="#333", fg="white",
                       activebackground="white", activeforeground="#333", command=self.curdWords).pack(side="left", padx=25)
        tkinter.Button(frame, text="猜单词游戏", width=25, height=7, bd=3, bg="#333", fg="white",
                       activebackground="white", activeforeground="#333", command=self.guessWords).pack(side="right",
                                                                                                   padx=25)
    #销毁GUI
    def destory(self):
        # 关闭当前窗口
        self.top.destroy()



