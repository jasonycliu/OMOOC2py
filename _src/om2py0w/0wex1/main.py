# -*-coding:utf-8 -*-
import time
'''交互101：极简交互式日记系统
*一次接收输入一行日记
*记录为本地文件
*再次运行系统时，能打印出过往的所有日志'''

''''
主要知识点:
.py 脚本 创建/管理/调用
.py 脚本 外部参数/数据 获取
中文 接收/打印
CLI 上的持续交互
数据文本 的创建/追加
数据文本 的循环读取
MyDailyCLI 私人记事本原型版'''

print "查看日记请输入read,记录日记请输入write."

command = raw_input('等待指令中...')

if command == 'read':
    fileobject = open('diary.txt','r')
    for eachline in fileobject:
        print eachline
    fileobject.close()
    
elif command == 'write':
    fileobject = open('diary.txt','a+')
    while True:
        text = raw_input('请输入日志内容,写完输入exit退出:')
        if text != 'exit':
            fileobject.write(time.strftime('%Y/%m/%d %H:%M:%S') + text +'\n')
        else:
            break
    fileobject.close()

else:
    print('抱歉,我们没能识别您的指令,系统将退出...')



