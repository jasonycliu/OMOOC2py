# -*- coding:utf-8 -*- 
#!/usr/bin/env python

'''
本周整体任务概述:

在上周开发基础上, 完成 极简交互式日记的桌面版本
需求如下:
每次运行时合理的打印出过往的所有日记
一次接收输入一行日记
保存为本地文件
时限: 1wd4~2wd3
发布: 发布到各自仓库的 _src/om2py2w/2wex0/ 目录中

脚本: main.py
日记文件:mydiary.txt

'''

import time
from Tkinter import * 

class App(Frame):
	
	#初始化frame
	def __init__(self,master=None):
		Frame.__init__(self,master)
		self.pack()
		self.createWidegets()

	#创建组件
	def createWidegets(self):

		self.label = Label(self,width='50',text="->(⊙o⊙)<-")
		self.label.pack()

		self.entry = Entry(self,width='50')
		self.entry.insert(0,'主人呢?!快来记日记啊!!')
		self.entry.pack()

		self.button = Button(self,text="QUIT",command=self.quit,anchor=E)
		self.button.pack(side=LEFT)

		#从本地读取文件
		self.readfile()

	def readfile(self):
		filetext = open('mydiary.txt','r').read()
		print filetext
		self.display = Label(self,bg='gray',text=filetext)
		self.display.pack()

root = Tk()
app = App(master=root)

app.mainloop()
root.destroy()