import os
import json
import BASE_bottle
import OAuth_ORG
from requests_oauthlib import OAuth1Session
from bottle import run,route,template,redirect,request,post
from bottle import TEMPLATE_PATH, jinja2_template as template
from collections import defaultdict

# index.pyが設置されているディレクトリの絶対パスを取得
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# テンプレートファイルを設置するディレクトリのパスを指定
TEMPLATE_PATH.append(BASE_DIR + "/views")

@route('/top0')
def get_search():
    #ツイッターAPIを取得する
    #OAuth_ORG.py を作成し、それぞれのキーを返すメソッドを用意すること。
    #git には加えてない（秘密鍵が漏れるの怖いので）
    CK = OAuth_ORG.OAuth_CK()
    CS = OAuth_ORG.OAuth_CS()
    AT = OAuth_ORG.OAuth_AT()
    AS = OAuth_ORG.OAuth_AS()
    twitter = OAuth1Session(CK, CS, AT, AS)

    terms = ['えみつん','アルバム','-RT']
    search_str=" AND ".join(terms)
    query = search_str
    params = {
        'q': query,
        'count': 20
    }

    #検索API の json URL を指定して、oAuth APIでゲットを行う
    url = 'https://api.twitter.com/1.1/search/tweets.json'
    req = twitter.get(url, params=params)

    result = []
    if req.status_code == 200:
        tweets = json.loads(req.text)
        result = tweets['statuses']
    else:
        print("ERROR!: %d" % req.status_code)
        result = None

    tables_rows = ""
    org_data = ""
    for r in result:
        tables_rows = tables_rows + "<tr>"
        for k,v in r.items():
            #org_data = org_data + str(k) + ":" + str(v) + "<br/>"
            if k in ['text','created_at']:
                tables_rows = tables_rows + "<td>" + str(v) + "</td>"
            if k == 'user':
                for k2,v2 in v.items():
                    if k2 == 'screen_name':
                        tables_rows = tables_rows + "<td>" + str(v2) + "</td>"
                    #org_data = org_data + "v2" + str(k2) + ":" + str(v2) + "<br/>"
                    # if k2 == 'user_mentions':
                    #     for k3,v3 in v2.items():
                    #         if k3 == 'screen_name':
                    #             tables_rows = tables_rows + "<td>" + str(v3) + "</td>"
        tables_rows = tables_rows + "</tr>"
    ret_text = template("top",query=query,tables=tables_rows,org_data=org_data)
    return ret_text        

if __name__ == "__main__":
    # localhost:8080 で公開するように実行
    run(host="localhost", port=8080, debug=True, reloader=True)
