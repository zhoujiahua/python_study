#!/usr/bin/python3
# -*- coding: UTF-8 -*-

from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def home():
    users = [
        {'id': 1, 'name': 'jiahua', 'age': 18, 'sex': 'male'},
        {'id': 2, 'name': 'Jerry', 'age': 28, 'sex': 'male'},
        {'id': 3, 'name': 'Jack', 'age': 38, 'sex': 'male'}
    ]
    return render_template('home.html', msg='Welcome to home page', users=users)

# 全局异常处理
# @app.errorhandler(404)
# def error_hand():
#     return render_template('404.html')


if __name__ == '__main__':
    port = 12306;
    app.run(port=port, debug=True)
