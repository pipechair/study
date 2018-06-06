# -*- coding: utf-8 -*-
import os
import json
import OAuth_ORG
import sqlite3  #sqlite3を私用する
from requests_oauthlib import OAuth1Session


#JSON によりログを取得する
def GetTwitterLog():
    