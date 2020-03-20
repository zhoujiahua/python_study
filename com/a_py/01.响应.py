#!/usr/bin/python3
# -*- coding: UTF-8 -*-

from flask import Flask, request, redirect, jsonify, render_template

app = Flask(__name__)


# 响应 html
@app.route('/')
def test():
    return '''
    <h1>Hello html</h1>
    '''


# 重定向
@app.route('/readhtml')
def readhtml():
    return redirect('https://www.baidu.com')


# 响应 json
@app.route('/strjson')
def strjson():
    user = {'id': 1, 'name': 'jiahua', 'age': 18, 'sex': 'male'}
    return jsonify(user)


# 响应页面
@app.route('/temp')
def temp():
    return render_template('hello.html', title='Hello python')


if __name__ == '__main__':
    port = 12306
    app.run(port=port, debug=True)
