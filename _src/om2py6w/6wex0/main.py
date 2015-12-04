# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup

HELP='''
        输入h打印帮助信息
        输入s,r,read,sync同步日记信息
        输入q退出日记软件
        输入del清空所有日记
    '''

#load_all_diary
def sync_diary():
   r = requests.get('http://jasonliu.sinaapp.com/')
   soup = BeautifulSoup(r.text,"html.parser")
   for item in soup.find_all("td","diary"):
        print item.text

#common line post请求写日记
def post_diary(diary,tag):
    params={'diary':diary,'tag':tag}
    r = requests.post('http://jasonliu.sinaapp.com/',data = params)
    print sync_diary()

#get diary by tag
def load_diary_by_tag(tag):
    if tag:
        #r = requests.get('http://jasonliu.sinaapp.com/tag/{}'.format(tag))
        r = requests.get('http://localhost:8080/tag/{}'.format(tag))
        soup = BeautifulSoup(r.text,"html.parser")
        for item in soup.find_all("td","diary"):
            print item.text
    else:
        sync_diary()

#delete all diary
def clear():
    r = requests.delete('http://jasonliu.sinaapp.com/')
    print "All diary had been clear......"

#输入q退出,s同步日记,h打印帮助信息,其他写日记
print HELP
tag = ''
while True:
    diary = raw_input("输入:")
    if diary.startswith('tag:'):
        tag = diary[4:]
    elif diary in ['exit','q','quit','out']:
        break
    elif diary in ['sync','r','s','read']:
        sync_diary()
    elif diary in ['help','h']:
        print HELP
    elif diary == 'del':
        confirm = raw_input("检测到您输入了del, 系统将要清空所有日记. 确定输入y, 取消输入n:")
        if confirm == 'y':
            clear()
        else:
            continue
    else:
        post_diary(diary,tag)