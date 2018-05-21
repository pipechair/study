import os
from bottle import run,route,template,redirect,request,post
from bottle import TEMPLATE_PATH, jinja2_template as template
from requests_oauthlib import OAuth1Session

def get_twitter_api():
    CK = 'cIHqS9ksIed3cSNQtn6w'                             # Consumer Key
    CS = '1S5MOs5k92YWbanjGWbUAFRuBOWRVbETYbJyBdZwZA'         # Consumer Secret
    AT = '15981126-15NKibLmlN0vhUyys4qYMJ7u51mf7PglKZlwWZVK6' # Access Token
    AS = '6gR2UNnwjkjUjMS8fwpGaejOCgqIDd4A4dD75WeJo2ybr'         # Accesss Token Secert
    twitter = OAuth1Session(CK, CS, AT, AS)
    return twitter