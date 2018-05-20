# -*- coding:utf-8 -*-
from bottle import route, run


@route('/hello')
def hello():
    return "Hello World!"

@route('/Test')
def test_route():
    return "<B>TEST!</B>"

#ダイナミックルーティング。URLに変数を仕込める
@route('/VAL/') #デフォルトの場合
@route('/VAL/<comment>')   #変数名は comment である
def view_val(comment='デフォルト'): #デフォルトの引数に 'デフォルト' を設定
    return '<I>{comment}</I>'.format(comment=comment)


#WEBサーバが立ち上がる。ブラウザからURLが入力されたらそれに対する処理を行う
run(host='localhost', port=8080, debug=True)
