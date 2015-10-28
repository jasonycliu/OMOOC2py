# -*- conding:utf-8 -*-
from Tkinter import *
from math import *

#entry 绑定事件
def evaluate(event):
    inputtext = str(eval(entry.get()))
    outputcontent = readfile() + inputtext + "\n"
    res.configure(text = outputcontent)
    writefile(outputcontent)

    #输入完日记并按回车后删除内容
    entry.delete(0, END)

#读取日记文件
def readfile():
    filetext = open('mydiary.txt','r').read()
    return filetext

#写日记文件
def writefile(outputcontent):
    fileobject = open('mydiary.txt','w+')
    fileobject.write(outputcontent)
    fileobject.close()

#初始化tk
w = Tk()

#创建组件
Label(w, text="my diary").pack()
entry = Entry(w)

#entry绑定回车按键，促发evaluate方法
entry.bind("<Return>", evaluate)
entry.pack()

#在label显示日记的内容
res = Label(w)
res.pack()
res.configure(text = readfile())

#quit退出按钮
quit = Button(w,text="QUIT",fg="red",command=w.quit)
quit.pack(side="left")

w.mainloop()
