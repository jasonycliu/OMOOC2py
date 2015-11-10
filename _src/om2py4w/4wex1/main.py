# -*- coding:utf-8 -*-

from bottle import route, request, debug, run, jinja2_view, static_file
from datetime import datetime, date

@route('/static/<filename>')
def server_static(filename):
    return static_file(filename,root='static')

#common line 读取数据
@route('/read')
def read_diary():
    f = open('mydiary.log')
    history = f.read()
    f.close()
    return history

#写日记函数
def write_diary(diarytext):
    date = datetime.now()
    dateformat = date.strftime('%Y-%m-%d: %H:%M:%S')
    with open('mydiary.log','a') as f:
        f.write('\n' + dateformat + ':' + diarytext)
        f.close()

#写日记的界面
@route('/', method='GET')
@jinja2_view('mydiary.html')
def log():
    mydiary = read_diary()
    return {'diary':unicode(mydiary,'utf-8')}

#提交日记的POST动作
@route('/', method='POST')    
@jinja2_view('mydiary.html')
def log():
    diary = request.forms.get('diary')
    write_diary(diary)
    mydiary = read_diary()
    return {'diary':unicode(mydiary,'utf-8')}

#启动内置sever
if __name__ == '__main__':
    debug(True)
    run(host='localhost',port=8080,reloader=True)
