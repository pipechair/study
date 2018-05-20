# -*- coding:utf-8 -*-
from bottle import route, run


@route('/hello')
def hello():
    return "Hello World!"

@route('/Test')
def test_route():
    return "<B>TEST!</B>"


run(host='localhost', port=8080, debug=True)
