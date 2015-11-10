# -*- coding:utf-8 -*-

from bottle import route, request, debug, run, jinja2_view, static_file
from datetime import datetime, date
import sqlite3

@route('/static/<filename>')
def server_static(filename):
    return static_file(filename,root='static')

#common line 读取数据
@route('/read')
def read_diary():
    conn = sqlite3.connect('mydiary.db')
    c = conn.cursor()
    c.execute("SELECT * from mydiary")
    mydiary = c.fetchall()
    print mydiary
    c.close()
    return mydiary

#写日记函数
def write_diary(diarytext):
    date = datetime.now()
    dateformat = date.strftime('%Y-%m-%d: %H:%M:%S')
    conn = sqlite3.connect('mydiary.db')
    c = conn.cursor()
    #diarytext加逗号解决Incorrect number of bindings supplied.
    c.execute("INSERT INTO mydiary (diary) VALUES (?)", (diarytext,))
    conn.commit()
    c.close()

#写日记的界面
@route('/', method='GET')
@jinja2_view('mydiary.html')
def log():
    mydiary = read_diary()
    return {'diarys':mydiary}

#提交日记的POST动作
@route('/', method='POST')    
@jinja2_view('mydiary.html')
def log():
    diary = request.forms.get('diary')
    #防止中文提交不了
    write_diary(unicode(diary,'utf-8'))
    mydiary = read_diary()
    return {'diarys':mydiary}

#启动内置sever
if __name__ == '__main__':
    debug(True)
    run(host='localhost',port=8080,reloader=True)
