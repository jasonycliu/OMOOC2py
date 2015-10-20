#-*-coding:utf-8-*-

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

from sys import argv

try:
    #如何输入的参数大于1,则是已经创建好文件,需要先读取原来的日志在记录日志.
    if len(argv) > 1 :
        filename = argv[1]
    else:
        filename = raw_input("请输入保存日志的文件名(如note.txt): ")

    fileobject = open(filename,'a+')  # a+ 表示以追加的模式打开,并且可以读写

    print "以下是您的日志记录:" + fileobject.read()

    #需要循环读取所以使用while循环,通过指定输入某个字符串退出,并保存日志
    while True:
        fileinput = raw_input("请输入日志内容:(输入exit退出) ")
        if fileinput != 'exit':
            fileobject.write(fileinput+"\n")
        else:
            break
finally:
    if fileobject:
        fileobject.close()
