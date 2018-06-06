# -*- coding: utf-8 -*-
import os
import json
import OAuth_ORG
from requests_oauthlib import OAuth1Session

#JSON によりログを取得する
def GetTwitterLog(stat):
    CK = OAuth_ORG.CK
    CS = OAuth_ORG.CS
    AT = OAuth_ORG.AT
    AS = OAuth_ORG.AS
    twitter = OAuth1Session(CK, CS, AT, AS)
    return twitter
