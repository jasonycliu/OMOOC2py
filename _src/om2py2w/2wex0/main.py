 #!/usr/bin/python
 # -*- coding: utf-8 -*-

from Tkinter import *
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

def evaluate(event):
    inputtext = str(entry.get())
    outputcontent = readfile() + inputtext + "\n"
    res.configure(text = outputcontent)
    writefile(outputcontent)
    entry.delete(0, END)

def readfile():
    filetext = open('mydiary.txt','r').read()
    return filetext

def writefile(outputcontent):
    fileobject = open('mydiary.txt','w+')
    fileobject.write(outputcontent)
    fileobject.close()

w = Tk()

Label(w, text="O(∩_∩)O").pack()
entry = Entry(w)
entry.bind("<Return>", evaluate)
entry.pack()

res = Label(w)
res.pack()
res.configure(text = readfile())

quit = Button(w,text="QUIT",fg="red",command=w.quit)
quit.pack(side="left")

w.mainloop()
