# -*- coding: utf-8 -*-
import os
from bottle import run,route,template,redirect,request,post
from bottle import TEMPLATE_PATH, jinja2_template as template
 
# index.pyが設置されているディレクトリの絶対パスを取得
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# テンプレートファイルを設置するディレクトリのパスを指定
TEMPLATE_PATH.append(BASE_DIR + "/views")
 
# 今回の場合は http://localhost:8080/top にアクセスが来た場合に公開する内容を指定。
# route関数をデコレータとして呼び出し、route関数の引数で/以降のアクセス先を指定する。
@route('/top')
def top():
    #return template('top') # template に対して設定した名前のファイルを開いて表示する。
    return template('mailform')

@route('/my-handling-form-page',method=["POST"])
def post_val():
    name_val = request.forms.name_val
    mail_val = request.forms.mail_val
    msg_val = request.forms.msg_val
    ret_text = template("form_out",name_val=name_val,mail_val=mail_val,msg_val=msg_val)
    return ret_text


if __name__ == "__main__":
    # localhost:8080 で公開するように実行
    run(host="localhost", port=8080, debug=True, reloader=True)

