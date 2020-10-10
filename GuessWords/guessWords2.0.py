#新功能：增加图形功能
import re
import tkinter


# 将句子转换成单词
def words(s, pattern = '[a-zA-Z-]+'):
  return re.findall(pattern, s)
# 创建python GUI
def createGUI():
    global top
    top = tkinter.Tk()
    # 设置窗口的大小
    top.wm_geometry("500x500+500+100")
    # 设置不允许改变窗口的高宽
    top.wm_resizable(False, False)
    # 设置窗口标题
    top.title('猜单词')
    createSubGroup()
    top.mainloop()
#   创建GUI当中的组件
def createSubGroup():
    global top

    label=tkinter.Label(top,text="请输入要导入的单词")
    label.pack()

    frame1 =tkinter.Frame(top)

    EditWords=tkinter.Entry(frame1,bd=5)
    EditWords.pack(side="left")

    button1=tkinter.Button(frame1,text="添加")
    button1.pack(side="center")





    # frame1.pack()
    frame1.pack()
    pass
top=None
createGUI()

