#!/usr/bin/python3
# -*- coding: UTF-8 -*-
from flask import Flask, render_template, jsonify
from urllib import request
from bs4 import BeautifulSoup

app = Flask(__name__)


# 数据获取
def get_data():
    url = 'https://search.51job.com/list/000000,000000,0000,00,9,99,Java%25E5%25BC%2580%25E5%258F%2591%25E5%25B7%25A5%25E7%25A8%258B%25E5%25B8%2588,2,1.html'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'}
    req = request.Request(url, headers=headers)
    res = request.urlopen(req)
    code = res.getcode()
    print(type(res))
    print(code)

    if code == 200:
        data = res.read()
        data = str(data, encoding='gbk')

        # 数据写入文件
        with open('./static/index.html', mode='w', encoding='gbk') as f:
            f.write(data)
            return True
    else:
        return False


# 处理数据
def parse_data():
    with open('./static/index.html', mode='r', encoding='gbk') as f:
        html = f.read()
        # 数据解析
        bs = BeautifulSoup(html, 'html.parser')
        # 查找数据
        # div = bs.find('div')
        # meta = bs.find_all('meta')
        # print(meta)
        # select() id class element
        # sec = bs.select('#work_position_click')
        # sec = sec[0].get_text().strip()
        # sec = sec[0].get_text(strip=True)
        # print(sec)

        # 获取列表信息
        lists = bs.select('#resultList .el')
        # print(lists)
        result = []
        for item in lists[1:]:
            title = item.select('.t1')[0].get_text(strip=True)
            company = item.select('.t2')[0].get_text(strip=True)
            address = item.select('.t3')[0].get_text(strip=True)
            salary = item.select('.t4')[0].get_text(strip=True)
            pubDate = item.select('.t5')[0].get_text(strip=True)
            # print(title, company, address, salary, pubDate)
            row = {
                'title': title,
                'company': company,
                'address': address,
                'salary': salary,
                'pubDate': pubDate
            }
            result.append(row)

        return result


# init data
@app.route('/')
def init_data():
    dataState = get_data()
    if dataState:
        return 'Data success'
    else:
        return 'No data'

# api data
@app.route('/api/list')
def list_data():
    data = parse_data()
    return jsonify(data)


if __name__ == '__main__':
    print(parse_data())
    port = 10000
    app.run(port=port, debug=True)
