#coding:utf-8
import os
import json
import OAuth_ORG
import sqlite3  #sqlite3を使用する
from requests_oauthlib import OAuth1Session

folder = os.path.dirname(os.path.abspath(__file__))
DATABASE = folder + '/samplex.db' #データベース名
conn = sqlite3.connect(DATABASE) #データベースへのコネクション

#JSON によりログを取得する
def get_twitter_log():
    CreateTable_()
    tw_session = OAuth_ORG.get_twitter_api() # Twitter のセッションを取得する
    # 特定のアカウントの情報を取得する
    params = {
        'screen_name': 'anisama',  # 取得するのスクリーンネーム
        'count': 100
    }
    end_point = 'https://api.twitter.com/1.1/statuses/user_timeline.json' #データ取得用のエンドポイント
    req = tw_session.get(end_point, params=params)   #リクエストを投げる

    if req.status_code == 200:
       tweets = json.loads(req.text)
       insert_main_data(tweets)
    else:
        print("ERROR!: %d" % req.status_code)
    
    
#SQLite3で、データを格納するためのテーブルを構築・挿入する
def insert_main_data(v_json):
    #取得した JSON の値をハッシュテーブルに対して格納していく
    c = conn.cursor()   #カーソルを取得
    t_status = v_json
    
    for st in t_status: #一ツイート分のデータが st に入っている。これを解析してテーブルにたたき込んでいく
        #SQL をデータから取得し作成する
        #GetInsertQuery(c,st)   #一ツイート分のデータをINSERTするクエリを生成
        id_val = st['id']
        text_val = st['text']
        value_text = (id_val,text_val,str(st))

        try:
            c.execute("INSERT INTO TBL_TWEET_INFO (id,tweet_text,JSON_DATA) VALUES (?,?,?)" ,value_text)
            conn.commit()
        except Exception as inst:
            print("Unexpected error:", inst)
        

        

#挿入用クエリ文字列を取得する
def get_insert_query(c,org_val):
    # org_val には一ツイート分のデータが dictionaly 形式で格納されている
    # 直接インサートしない列名をタプルに用意する
    column_name = ''

    #id を取得
    id_val = org_val['id']
    text_val = org_val['text']
    value_text = (id_val,text_val,'',)

    try:
        c.execute("INSERT INTO TBL_TWEET_INFO (id,tweet_text,JSON_DATA) VALUES (?,?,?)" ,value_text)
    except Exception as inst:
        print("Unexpected error:", inst)

    return 

def get_twitter_log_info():
    # 取得したTwitterのログを生のママ保存する。
    # 保存する際、TweetのIDはキーの情報として別の列に保存する。
    # また、IDが取得できなかったときのため、一応IDENTITY列を一つ用意する。
    create_info_table() # テーブルを作成する
    tw_session = OAuth_ORG.get_twitter_api() # Twitter のセッションを取得する
    # 特定のアカウントの情報を取得する
    params = {
        'screen_name': 'anisama',  # 取得するのスクリーンネーム
        'count': 100
    }
    end_point = 'https://api.twitter.com/1.1/statuses/user_timeline.json' #データ取得用のエンドポイント
    req = tw_session.get(end_point, params=params)   #リクエストを投げる

    if req.status_code == 200:
       tweets = json.loads(req.text)
       insert_main_data(tweets)
    else:
        print("ERROR!: %d" % req.status_code)



def create_info_table():
    # TWEET の値を格納するためのテーブル
    query1 = '''CREATE TABLE IF NOT EXISTS TBL_TWEET_INFO 
    ( 
    uniq INTEGER PRIMARY KEY, 
    id INTEGER, 
    tweet_text TEXT,
    JSON_DATA TEXT
    ) '''
    c = conn.cursor()   #カーソルを取得
    c.execute(query1)   # SQLの実行


if __name__ == '__main__':
    get_twitter_log_info()
