#coding:utf-8
import os
import json
import OAuth_ORG
import sqlite3  #sqlite3を使用する
from requests_oauthlib import OAuth1Session

folder = os.path.dirname(os.path.abspath(__file__))
DATABASE = folder + '/sample.db' #データベース名
conn = sqlite3.connect(DATABASE) #データベースへのコネクション

#JSON によりログを取得する
def GetTwitterLog():
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
       InsertMainData(tweets)
    else:
        print("ERROR!: %d" % req.status_code)
    
    
#SQLite3で、データを格納するためのテーブルを構築・挿入する
def InsertMainData(v_json):
    #取得した JSON の値をハッシュテーブルに対して格納していく
    c = conn.cursor()   #カーソルを取得
    t_status = v_json
    for st in t_status: #一ツイート分のデータが st に入っている。これを解析してテーブルにたたき込んでいく
        #SQL をデータから取得し作成する
        query= GetInsertQuery(st)
        c.execute(query)   # SQLの実行     
    c.commit

        
def CreateTable_():
    # TWEET の値を格納するためのテーブル
    query1 = '''CREATE TABLE IF NOT EXISTS TBL_TWEET 
    ( 
    uniq INTEGER PRIMARY KEY, 
    created_at NONE, 
    id NONE, 
    id_str TEXT, 
    text TEXT,
    truncated NONE, 
    source NONE, 
    in_reply_to_status_id NONE, 
    in_reply_to_status_id_str TEXT, 
    in_reply_to_user_id NONE,
    in_reply_to_user_id_str TEXT, 
    in_reply_to_screen_name TEXT, 
    geo NONE, 
    coordinates NONE, 
    place None, 
    contributors None, 
    is_quote_status None, 
    retweet_count INTEGER, 
    favorite_count INTEGER, 
    favorited NONE, 
    retweeted NONE, 
    possibly_sensitive NONE, 
    lang NONE 
    ) '''
    c = conn.cursor()   #カーソルを取得
    c.execute(query1)   # SQLの実行

    #ユーザーの情報を格納するテーブルを作成
    #Tweetの Id をキーとして保存する
    #Tweetを取得したときのUser情報を残すため
    query2 = '''
        CREATE TABLE IF NOT EXISTS TBL_USER(
        uniq INTEGER PRIMARY KEY,
        id  INTEGER, 
        id_str  TEXT, 
        name  TEXT, 
        screen_name  TEXT,
        location  NONE,
        description  TEXT, 
        url  TEXT, 
        protected  NONE, 
        followers_count  INTEGER, 
        friends_count  INTEGER, 
        listed_count  INTEGER, 
        created_at  NONE, 
        favourites_count  INTEGER, 
        utc_offset  INTEGER, 
        time_zone  TEXT, 
        geo_enabled  NONE, 
        verified  NONE, 
        statuses_count  INTEGER, 
        lang  TEXT, 
        contributors_enabled  NONE, 
        is_translator  NONE, 
        is_translation_enabled  NONE, 
        profile_background_color  TEXT, 
        profile_background_image_url  TEXT,
        profile_background_image_url_https  TEXT, 
        profile_background_tile  NONE, 
        profile_image_url  TEXT, 
        profile_image_url_https  TEXT, 
        profile_banner_url  TEXT, 
        profile_link_color  TEXT, 
        profile_sidebar_border_color  TEXT, 
        profile_sidebar_fill_color  TEXT, 
        profile_text_color  TEXT, 
        profile_use_background_image  NONE, 
        has_extended_profile  NONE, 
        default_profile  NONE, 
        default_profile_image  NONE, 
        following  NONE, 
        follow_request_sent  NONE, 
        notifications  NONE, 
        translator_type  TEXT
    )
    '''
    c.execute(query2)   # SQLの実行   
    conn.commit

#挿入用クエリ文字列を取得する
def GetInsertQuery(org_val):
    # 直接インサートしない列名をタプルに用意する
    Exclusion_column = ('entities','metadata','user','retweeted_status')
    column_name = ''
    values_str = ''
    for key,value in org_val.items():
        if Exclusion_column.__contains__(key):
            pass    #なにもしない
        else:
            if len(column_name) > 0 :
                column_name = column_name + ','
            column_name = column_name + "'{0}'".format(key)
            if len(values_str) > 0 :
                values_str = values_str + ','
            values_str = values_str + "'{0}'".format(value)

        # JSON で取得したデータのカラム名と値を取得して、INSERT に使用する
        # 一部は使用しないので対象外とする
    ret_query = 'INSERT INTO TBL_TWEET ({0}) VALUES ({1})'.format(column_name,values_str)
    return ret_query

GetTwitterLog()