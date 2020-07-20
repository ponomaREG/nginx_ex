# -*- coding: utf-8 -*-

from app import app
from flask import jsonify, request
from PIL import Image
import pytesseract
import pyocr
import pyocr.builders
from werkzeug.utils import secure_filename
import os
import io
import sqlite3
import datetime

basedir = os.path.join('static','images')
app.config['UPLOAD_FOLDER'] = os.path.join(os.path.abspath(os.path.dirname(__file__)),basedir)
app.config['JSON_AS_ASCII'] = False
basedir = os.path.abspath(os.path.dirname(__file__))

app.config['JSON_AS_ASCII'] = False
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///' + os.path.join(basedir, 'db.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db = sqlite3.connect(os.path.join(basedir, 'stat.db'), check_same_thread=False)
@app.route('/', methods = ['GET'])
def index():
    return jsonify({'status':'Oh,Hi mark!'})

@app.route('/test', methods = ['GET'])
def test():
    return '<h1>TE123123123123123123123123123123123123123123123123123123123123123123123123123123123123123123123123123123123123123123123123123123123123123123123123123123123123123123123123123123123123123123123123123123123123123123123123123123123123123123123123123123123123123123123123123123123123123123123123123123123123123123123123123123123123123123123123123123123123123123123123123123123ST</h1>'


@app.route('/stat/add')
def testIP():
        if request.headers.getlist("X-Forwarded-For"):
           ipuser = request.headers.getlist("X-Forwarded-For")[0]
        else:
           ipuser = request.remote_addr

        test = request.args.get('test',type=str,default='Null')
        result = request.args.get('result',type=int,default=-1)
        date = datetime.datetime.now()
        db.execute("INSERT into stat values(NULL,'{}','{}',{},'{}')".format(ipuser,test,result,date))
        db.commit()
        return jsonify({'status':1})

@app.route('/stat/unique/<string:column>')
def getUniqueRowsByColumn(column):
    sql_query = 'select DISTINCT {} from stat;'
    result_js = {}
    result_js['data'] = []
    cursor = None
    try:
        cursor = db.execute(sql_query.format(column))
    except:
        result_js['status'] = -1
        return jsonify(result_js)
    result_query = cursor.fetchall()
    lenght = len(result_query)
    result_js['count'] = lenght
    if lenght == 0:
        result_js['status'] = 0
        return jsonify(result_js)
    for row in result_query:
        result_js['data'].append(row[0])
    result_js['status'] = 1
    return jsonify(result_js)

@app.route('/stat/unique')
def getUniqueColumns():
    sql_query = "PRAGMA table_info(stat);"
    cursor = db.execute(sql_query)
    result_js = {}
    result_js['status'] = 1
    result_js['data'] = []
    result_js['desc'] = 'Available columns in "stat"'
    for row in cursor.fetchall():
        result_js['data'].append(row[1])
    return jsonify(result_js)

@app.route('/stat/get')
def getStat():
    cursor = db.execute("select * from stat")
    result = []
    counter = 0
    for rv in cursor.fetchall():
        result.append({'id':rv[0],'user':rv[1],'test':rv[2],'result':rv[3],'date':rv[4]})
        counter+=1
    return jsonify({'status':1,'result':result,'count':counter})


@app.route('/upload', methods = ['GET', 'POST'])
def upload():
    if request.method == 'POST':
        if 'file' not in request.files:
            return jsonify({"status":0})
        file = request.files['file']
        if file.filename == '':
            return jsonify({'status':0})
        if file:
            filename = secure_filename(file.filname)
            path_to_image = os.path.join(os.getcwd(),"nginx_ex",app.config['UPLOAD_FOLDER'],filename)
            file.save(path_to_image)
            tool = pyocr.get_available_tools()[0]
            lang = str(tool.get_available_languages())
            text = '123'
            text = tool.image_to_string(Image.open(path_to_image),builder = pyocr.builders.TextBuilder(),lang='rus')
            return jsonify({'status':1,'text':text,lang:lang})
    return '''
        <!doctype html>
        <title>Upload new File</title>
        <h1>Upload new File</h1>
        <form method=post enctype=multipart/form-data>
        <input type=file name=file>
        <input type=submit value=Upload>
        </form>
        '''

