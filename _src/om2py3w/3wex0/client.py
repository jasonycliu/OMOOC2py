#!/usr/bin/env python
# -*- coding: utf-8 -*-
import socket

HOST = '127.0.0.1'
PORT = 9999

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)


#运行程序打印帮助信息
s.sendto('h',(HOST,PORT))
print s.recv(1024)
#运行程序打印历史日记
s.sendto('r',(HOST,PORT))
print s.recv(1024)

while True:
	inputtext = raw_input("请输入日记->")
	#发送消息
	s.sendto(inputtext,(HOST,PORT))
	#输入q退出客户端
	if(inputtext == 'q'):
		break
	else:
		#接收消息
		data = s.recv(1024)
		print data
s.close()