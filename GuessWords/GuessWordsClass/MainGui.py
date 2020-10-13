import tkinter
import tkinter.messagebox
class mainGui:
    root=None
    def __init__(self):
        self.createGUI()
    # 单词操作按钮关联函数
    def curdWords(self):
        # 销毁当前GUI
        self.destory()
        # 创建单词操作GUI
        from GuessWords.GuessWordsClass.CurdWordsGui import curdWordsGui
        curdWordsGui()


    # 猜单词游戏按钮关联函数
    def guessWords(self):
        from GuessWords.GuessWordsClass.GuessWordsGui import guessWordsGui

        # 弹框
        if  tkinter.messagebox.askquestion("选择存储方式", "请问您是否使用文本存储的单词表来进行游戏？\n（选择“是”使用文本，选择“否”使用数据库）")=="yes":
            # 销毁当前GUI
            self.destory()
            # 创建猜单词游戏GUI
            guessWordsGui(bottomMenvRBVNum=1)

        else:
            # 销毁当前GUI
            self.destory()
            # 创建猜单词游戏GUI
            guessWordsGui(bottomMenvRBVNum=2)






    # 创建python GUI
    def createGUI(self):
        self.root = tkinter.Tk()
        # 设置窗口的大小
        self.root.wm_geometry("500x300+500+100")
        # 设置不允许改变窗口的高宽
        self.root.wm_resizable(False, False)
        # 设置窗口标题
        self.root.title('单词猜猜猜')
        self.createSubGroup()
        self.root.mainloop()

    #   创建GUI当中的组件
    def createSubGroup(self):
        frame = tkinter.Frame(self.root).pack(fill="both")
        tkinter.Button(frame, text="<——词库操作——>", width=25, height=7, bd=3, bg="#333", fg="white",
                       activebackground="white", activeforeground="#333", command=self.curdWords).pack(side="left", padx=25)
        tkinter.Button(frame, text="<——猜单词游戏——>", width=25, height=7, bd=3, bg="#333", fg="white",
                       activebackground="white", activeforeground="#333", command=self.guessWords).pack(side="right",
                                                                                                   padx=25)
    #销毁GUI
    def destory(self):
        # 关闭当前窗口
        self.root.destroy()



