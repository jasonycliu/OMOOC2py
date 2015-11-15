#!/usr/bin/env python
# -*- coding: utf-8 -*-
import socket

#创建一个客户端的基于TCP 协议的socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#建立连接
s.connect(('127.0.0.1',9999))

#运行程序打印历史日记
#s.send('r')
#print s.recv(1024)

while True:
	inputtext = raw_input("请输入日记->")
	if(inputtext == 'q'):
		break
	#发送消息
	s.send(inputtext)
	#接收消息
	data = s.recv(1024)
	print data
s.close()
