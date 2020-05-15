from app import app
from flask import jsonify
import os


@app.route('/', methods = ['GET'])
def index():
    return jsonify({'status':'Oh,Hi mark!'})

@app.route('/test', methods = ['GET'])
def test():
    return '<h1>TEST</h1>'

@app.route('/file', methods = ['GET'])
def getFile():
    baseDir =  os.path.abspath(os.path.dirname(__file__))
    path = os.path.join(baseDir,"touch.txt")
    file = open(path, 'r')
    text = file.read()
    file.close()
    return jsonify({'text':text})




@app.route('/newMethod',methods=['GET'])
def function142945():
	return '<h1>Oh, hi mark</h1>'
@app.route('/newMethod2',methods=['GET'])
def function101454():
	return '<h1>Oh, hi mark</h1>'
@app.route('/newMethod2',methods=['GET'])
def function131567():
	return '<h1>Oh, hi mark</h1>'
@app.route('/newMethod2',methods=['GET'])
def function117813():
	return '<h1>Oh, hi mark</h1>'
@app.route('/m',methods=['GET'])
def function157939():
	return '<h1>Oh, hi mark</h1>'
@app.route('/me',methods=['GET'])
def function150713():
	return '<h1>Oh, hi mark</h1>'
@app.route('/met',methods=['GET'])
def function105581():
	return '<h1>Oh, hi mark</h1>'
@app.route('/met',methods=['GET'])
def function134209():
	return '<h1>Oh, hi mark</h1>'
@app.route('/met',methods=['GET'])
def function149332():
	return '<h1>Oh, hi mark</h1>'
@app.route('/mettt',methods=['GET'])
def function150756():
	return '<h1>Oh, hi mark</h1>'
@app.route('/methods',methods=['GET'])
def function116403():
	return '<h1>Oh, hi mark</h1>'
@app.route('/methods',methods=['GET'])
def function107798():
	return '<h1>Oh, hi mark</h1>'
@app.route('/etr',methods=['GET'])
def function147149():
	return '<h1>Oh, hi mark</h1>'
@app.route('/etr123',methods=['GET'])
def function113100():
	return '<h1>Oh, hi mark</h1>'
@app.route('/e',methods=['GET'])
def function173466():
	return '<h1>Oh, hi mark</h1>'
@app.route('/e',methods=['GET'])
def function178743():
	return '<h1>Oh, hi mark</h1>'
@app.route('/easd',methods=['GET'])
def function153245():
	return '<h1>Oh, hi mark</h1>'
@app.route('/easdasd',methods=['GET'])
def function187674():
	return '<h1>Oh, hi mark</h1>'
@app.route('/123',methods=['GET'])
def function185874():
	return '<h1>Oh, hi mark</h1>'