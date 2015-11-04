#!/usr/bin/env python
# -*- coding: utf-8 -*-
import socket

HOST = '127.0.0.1'
PORT = 9999

#创建一个客户端的基于TCP 协议的socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#建立连接
#s.connect(HOST,PORT)
s.connect((HOST,PORT))

#接收服务的欢迎信息
print s.recv(1024)

#运行程序打印历史日记
s.send('r')
print s.recv(1024)

while True:
	inputtext = raw_input("请输入日记->")
	#发送消息
	s.send(inputtext)
	#输入q退出客户端
	if(inputtext == 'q'):
		break
	else:
		#接收消息
		data = s.recv(1024)
		print data
s.close()