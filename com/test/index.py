#!/usr/bin/python3
# -*- coding: UTF-8 -*-

from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def hello_world():
    return '<h1>波波来吃鸡，我们开挂横着走！</h1>'


@app.route('/welcome')
def welcome():
    return '<h2>哟西。。。。。</h2>'


# Get request
@app.route('/info')
def info():
    a = request.args.get('a', default=111)
    b = request.args.get('b', default=666)
    print(a + b)
    return 'get info .....' + a + b


# start server
if __name__ == '__main__':
    app.debug = True
    port = 8888
    app.run(port=port)
