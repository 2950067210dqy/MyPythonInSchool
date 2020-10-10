import tkinter as tk

def button_clicked():
    listbox.delete(0,4)
    count1 = float(enrty1.get())
    count2 = float(enrty2.get())
    count3 = float(enrty3.get())
    text="名称  单价  数量  价格"
    text1="苹果 "+str(apple)+"元  "+str(count1)+"k "+str(apple*count1)+"元"
    text2="梨子 "+str(pear)+"元  "+str(count2)+"k "+str(pear*count2)+"元"
    text3="香蕉 "+str(bana)+"元  "+str(count3)+"k "+str(bana*count3)+"元"
    text4="总价 "+str(int(apple*count1+pear*count2+bana*count3))+"元"
    listbox.insert(0,text)
    listbox.insert(1,text1)
    listbox.insert(2, text2)
    listbox.insert(3, text3)
    listbox.insert(4, text4)
apple=6.5
pear=5.4
bana=7.2
top=tk.Tk()
top.title("便捷水果店")
top.geometry("300x350")
label1=tk.Label(top,text="请输入苹果的重量:")
label1.pack()
enrty1=tk.Entry(top)
enrty1.pack()
label2=tk.Label(top,text="请输入梨子的重量:")
label2.pack()
enrty2=tk.Entry(top)
enrty2.pack()
label3=tk.Label(top,text="请输入香蕉的重量:")
label3.pack()
enrty3=tk.Entry(top)
enrty3.pack()
listbox=tk.Listbox(top)
listbox.pack()
btn=tk.Button(top,text="结算",command=button_clicked)
btn.pack()
top.mainloop()

