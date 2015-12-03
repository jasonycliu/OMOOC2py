# -*- coding: utf-8 -*-

from bottle import route, Bottle, run, jinja2_view, request, static_file, debug
import sae
import sae.kvdb
import sys
from time import localtime, strftime

reload(sys)
sys.setdefaultencoding('utf-8')
count = 0

app = Bottle()
debug(True)  #打开debug功能

kv = sae.kvdb.KVClient()

#load static files
@app.route('/static/<filename>')
def server_static(filename):
    print (filename)
    return static_file(filename,root='static')

#load all diary
def load_all_diary():
    diarys = []
    for key in list (kv.get_by_prefix("diary")):
        diarys.append(key[1])
    diarys = sorted(diarys, key = lambda x:x['time'], reverse=True)
    return diarys

#write diary to kvdb
def write_diary(input_diary,tag):
    global count
    key = "diary" + str(count)
    time = strftime('%Y-%m-%d %H:%M:%S',localtime())
    diary = {"time":time,"diary":input_diary,"tag":tag}
    kv.set(key,diary)
    print kv
    count += 1

#get value by tag
def get_tag_value(tag):
    #当kvdb存在tag时,获取所有的tag
    print(tag)
    if kv.get(tag):
        print(tag)
        keys = kv.get(tag)
        #返回key/value 的dict
        tmp = kv.get_multi(keys)
        #遍历dict并返回list格式(tag的所有value)
        results = [tmp[key] for key in tmp.keys()]
        return results
    else:
        return None

#delete key
@app.route('/',method = 'DELETE')
def delete():
    keys = kv.getkeys_by_prefix("diary")
    for key in keys:
        kv.delete(key)

#index of mydiary
@app.route('/',method='GET')
@jinja2_view('mydiary.html')
def log():
    diarys = load_all_diary()
    return {'diarys':diarys}

#method for POST request
@app.route('/', method='POST')
@jinja2_view('mydiary.html')
def log():
    diary = request.forms.get('diary')
    tag   = request.forms.get('tag')
    write_diary(diary,tag)
    diarys = load_all_diary()
    return {'diarys':diarys}

#get diarys by tag
@app.route('/tags/:tag')  #old syntax 
@jinja2_view('diary_by_tag.html')
def get_value_by_tag(tag):
    mydiarys = get_tag_value(tag)
    print mydiarys
    if mydiarys:
        return {'diarys':mydiarys, 'tag':tag}
    else:
        return "标签不存在,<a href='/'>请返回!</a>"

application = sae.create_wsgi_app(app)
