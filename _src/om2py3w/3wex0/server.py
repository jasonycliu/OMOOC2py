#!/usr/bin/env python
# -*- coding:utf-8 -*-
import socket

HOST = '127.0.0.1'
PORT = 9999

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind((HOST,PORT))

print '等待客户端输入日记...'

outputtext = ""

def read():
	with open('mydiary.log','r') as history:
		return history.read()

def write(outputtext):
	with open('mydiary.log','a+') as f:
		f.write(outputtext)

while True:
	data,addr = s.recvfrom(1024)
	#当获取的指令为r时,客户端同步数据
	if(data == 'r'):
		history = read()
		s.sendto(history,addr)

	#当指令为h时,客户端打印当前帮助信息
	elif(data == 'h'):
		helptext = '\n'.join(['输入[q]退出程序','输入[r]同步历史笔记','输入[h]打印当前日记'])
		s.sendto(helptext,addr)
		
	else:
		outputtext += '\n' + data
		with open('mydiary.log','w') as f:
			f.write(outputtext)
		s.sendto(outputtext,addr)
s.close