from flask import Flask, jsonify,request
from app import app
import random
import os,subprocess


@app.route('/',methods=['GET'])
def getFrame2():
    text = request.args.get('text',default = 'default',type = str)
    path = '/home/user/nginx_ex/app/touch.txt'
    file = open(path,"w")
    file.write(text)
    file.close()
    return jsonify({'text':text})

@app.route('/newMethod',methods=['GET'])
def addNewMethod():
    text = request.args.get('text',default = '<h1>Oh, hi mark</h1>', type = str)
    route = request.args.get('route',type = str)
    path = '/home/user/nginx_ex/app/views.py'
    function_name = random.randint(100000,200000)
    function_name = "function" + str(function_name)
    function = "\n@app.route('/{}',methods=['GET'])\ndef {}():\n\treturn '{}'".format(route, function_name, text)

    views_back = open(path,'a')
    views_back.write(function)
    views_back.close()
    subprocess.call('sudo service restart nginx_ex.service',shell = True)
    return ({'text' : text})


