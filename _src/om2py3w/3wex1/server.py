#!/usr/bin/env python
# -*- coding:utf-8 -*-
import socket
import time
import threading

HOST = '127.0.0.1'
PORT = 9999

#创建TCP socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#绑定端口
s.bind((HOST,PORT))

#监听端口,并设置等待连接的最大数为5
s.listen(5)

print '等待客户端输入日记...'

outputtext = ""

#读取历史日记文件
def read():
	with open('mydiary.log','r') as history:
		return history.read()

#输出日记文件到系统当前目录
def write(outputtext):
	with open('mydiary.log','a+') as f:
		f.write(outputtext)

def tcp(sock,addr):
	print '接收到来自 %s:%s...' % addr
	sock.send("欢迎使用日记本...")
	
	while True:
		data = s.recv(1024)
		time.sleep()
		#当获取的指令为r时,客户端同步数据
		if(data == 'r'):
			history = read()
			sock.send(history,addr)

		#当指令为h时,客户端打印当前帮助信息
		elif(data == 'h'):
			helptext = '\n'.join(['输入[q]退出程序','输入[r]同步历史笔记','输入[h]打印当前日记'])
			sock.send(helptext,addr)
			
		else:
			outputtext += '\n' + data
			#写数据到文件中
			write(outputtext)
			sock.send(outputtext,addr)
	sock.close
	print '来自 %s:%s 请求已经关闭.' % addr

#服务端通过一个永久循环来接收消息
while True:
	#accept 接收一个客户的连接并返回
	sock,addr = s.accept()
	# 创建新线程来处理TCP连接: 否则在处理的过程中无法处理其他的客户端请求	
    	t = threading.Thread(target=tcp, args=(sock, addr))
    	t.start()
