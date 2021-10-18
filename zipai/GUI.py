from zipai.player import player
from zipai.poke import poke
import tkinter
class gui:
    def __init__(self):
        self.createGui()
    def createGui(self):
        self.root = tkinter.Tk()
        # 设置窗口的大小
        self.root.wm_geometry("900x700+400+50")
        # 设置不允许改变窗口的高宽
        self.root.wm_resizable(False, False)
        # 设置窗口标题
        self.root.title('打牌游戏')
        self.createSubGui()
        self.root.mainloop()
    def createSubGui(self):
        mainframe=tkinter.Frame(self.root)
        titlelabel=tkinter.Label(mainframe,text="123123")
        titlelabel.pack(fill="x")

        mainframe.pack(fill="both")




        pass

gui()