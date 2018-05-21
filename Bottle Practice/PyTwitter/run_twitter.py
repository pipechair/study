#!/usr/bin/env python
# -*- coding: utf-8 -*-

from requests_oauthlib import OAuth1Session

CK = 'cIHqS9ksIed3cSNQtn6w'                             # Consumer Key
CS = '1S5MOs5k92YWbanjGWbUAFRuBOWRVbETYbJyBdZwZA'         # Consumer Secret
AT = '15981126-15NKibLmlN0vhUyys4qYMJ7u51mf7PglKZlwWZVK6' # Access Token
AS = '6gR2UNnwjkjUjMS8fwpGaejOCgqIDd4A4dD75WeJo2ybr'         # Accesss Token Secert

# ツイート投稿用のURL
url = "https://api.twitter.com/1.1/statuses/update.json"

# ツイート本文
params = {"status": "パイソンを使ったテスト投稿です"}

# OAuth認証で POST method で投稿
twitter = OAuth1Session(CK, CS, AT, AS)
req = twitter.post(url, params = params)

# レスポンスを確認
if req.status_code == 200:
    print ("OK")
else:
    print ("Error: %d" % req.status_code)