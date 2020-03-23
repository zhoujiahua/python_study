#!/usr/bin/python3
# -*- coding: UTF-8 -*-

from flask import Flask, jsonify, render_template
import mysql.connector
import json

app = Flask(__name__)


@app.route('/')
def home_index():
    # dbcursor.execute("CREATE TABLE sites (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), url VARCHAR(255))")
    update_data()
    return 'Hello World'


@app.route('/list')
def list_page():
    data = list_data()
    return render_template('list.html', list=data, msg='List')


@app.route('/api/list')
def api_list():
    data = list_data()
    return jsonify(data)


def list_data():
    mydb = db_connect()
    mycursor = mydb.cursor()
    sql = 'SELECT * FROM sites'
    mycursor.execute(sql)
    data = mycursor.fetchall()
    print(data)
    return data


def db_connect():
    db = mysql.connector.connect(
        host="localhost",  # 数据库主机地址
        user="root",  # 数据库用户名
        passwd="123456",  # 数据库密码
        database="python"  # 数据库
    )
    dbcursor = db.cursor()
    print(dbcursor)
    return db


def update_data():
    mydb = db_connect()
    mycursor = mydb.cursor()
    sql = "INSERT INTO sites (name, url) VALUES (%s, %s)"
    val = [
        ('Google', 'https://www.google.com'),
        ('Github', 'https://www.github.com'),
        ('Taobao', 'https://www.taobao.com'),
        ('stackoverflow', 'https://www.stackoverflow.com/')
    ]
    mycursor.executemany(sql, val)
    mydb.commit()  # 数据库事务提交
    print(mycursor.rowcount, "记录插入成功。")


if __name__ == '__main__':
    app.run(port=12345, debug=True)
