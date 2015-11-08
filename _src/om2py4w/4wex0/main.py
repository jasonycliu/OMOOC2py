# -*- coding:utf-8 -*-
from bottle import route, template, request, debug, run 
from datetime import datetime, date

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
def log():
    mydiary = read_diary()
    return template('mydiary',diary=mydiary)

#提交日记的POST动作
@route('/', method='POST')    
def log():
    diary = request.forms.get('diary')
    write_diary(diary)
    mydiary = read_diary()
    return template('mydiary',diary=mydiary)

#启动内置sever
if __name__ == '__main__':
    debug(True)
    run(host='localhost',port=8080,reloader=True)
