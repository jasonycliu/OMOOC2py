#!/usr/bin/env python
# -*-coding: utf-8 -*-
import urllib

HELP='''
        输入h打印帮助信息
        输入s同步日记信息
        输入q退出日记软件
    '''

#common line get请求读取日记信息
def sync_diary():
    req = urllib.urlopen('http://localhost:8080/read')
    res = req.read()
    print res

#common line post请求写日记
def post_diary(diary):
    params={}
    params['diary'] = diary
    params = urllib.urlencode(params)
    urllib.urlopen('http://localhost:8080/',params)
    print sync_diary()

#输入q退出,s同步日记,h打印帮助信息,其他写日记
while True:
    input_text = raw_input("输入:")
    if(input_text == 'q'):
        break
    elif(input_text == 's'):
        sync_diary()

    elif(input_text == 'h'):
        print HELP
    else:
        post_diary(input_text)