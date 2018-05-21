import os
import json
import BASE_bottle
from requests_oauthlib import OAuth1Session
from bottle import run,route,template,redirect,request,post
from bottle import TEMPLATE_PATH, jinja2_template as template
from collections import defaultdict

# index.pyが設置されているディレクトリの絶対パスを取得
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# テンプレートファイルを設置するディレクトリのパスを指定
TEMPLATE_PATH.append(BASE_DIR + "/views")

#ツイッターAPIを取得する
CK = 'cIHqS9ksIed3cSNQtn6w'                             # Consumer Key
CS = '1S5MOs5k92YWbanjGWbUAFRuBOWRVbETYbJyBdZwZA'         # Consumer Secret
AT = '15981126-15NKibLmlN0vhUyys4qYMJ7u51mf7PglKZlwWZVK6' # Access Token
AS = '6gR2UNnwjkjUjMS8fwpGaejOCgqIDd4A4dD75WeJo2ybr'         # Accesss Token Secert
twitter = OAuth1Session(CK, CS, AT, AS)

terms = ['えみつん','アルバム']
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
    #print("検索結果:" + str(result))
else:
    print("ERROR!: %d" % req.status_code)
    result = None

for r in result:
    for k,v in r.items():
        if k in ['text', 'retweet_count', 'favorite_count', 'id', 'created_at']:
            print(k+':')
            print(v)
            print('    ')
    print('-----------------------------------------------------------------')


