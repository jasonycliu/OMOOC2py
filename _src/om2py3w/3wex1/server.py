#!/usr/bin/env python
# -*- coding:utf-8 -*-
import socket,time,threading

#读取历史日记文件
def read():
	with open('mydiary.log','r') as history:
		return history.read()

#输出日记文件到系统当前目录
def write(outputtext):
	with open('mydiary.log','a+') as f:
		f.write(outputtext)

def tcp(sock,addr):

	outputtext = ""
	print '接收到来自 %s:%s...' % addr

	while True:
		data = sock.recv(1024)
		
		#当获取的指令为r时,客户端同步数据
		if(data == 'r'):
			history = read()
			sock.send(history)

		#当指令为h时,客户端打印当前帮助信息
		elif(data == 'h'):
			helptext = '\n'.join(['输入[q]退出程序','输入[r]同步历史笔记','输入[h]打印当前日记'])
			sock.send(helptext)
			
		else:
			outputtext += '\n' + data
			#写数据到文件中
			write(outputtext)
			if(data != 'q'):
				sock.send(outputtext)

#创建TCP socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#绑定端口
s.bind(('127.0.0.1',9999))

#监听端口,并设置等待连接的最大数为5
s.listen(5)

#服务端通过一个永久循环来接收消息
while True:
	#accept 接收一个客户的连接并返回
	sock,addr = s.accept()
	# 创建新线程来处理TCP连接: 否则在处理的过程中无法处理其他的客户端请求	
	t = threading.Thread(target=tcp, args=(sock, addr))
	t.start
