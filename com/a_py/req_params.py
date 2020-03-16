#!/usr/bin/python3
# -*- coding: UTF-8 -*-

from flask import Flask, request

app = Flask(__name__)


# Home page
@app.route('/')
def index():
    return 'Hello Index'


# Get info
@app.route('/get_info')
def get_info():
    a = request.args.get('a', default=111)
    b = request.args.get('b', default=222)
    return 'Hello Info' + str(a) + str(b)


# Post info
@app.route('/post_info', methods=['get', 'post'])
def post_info():
    a = request.form['a']
    b = request.form['b']
    return a + b


if __name__ == '__main__':
    app.run(debug=True)
