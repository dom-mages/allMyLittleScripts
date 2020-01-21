#!/usr/bin/env python3
# simple script without much effort in parsing the cl arguments because it will be called from bash wrapper functions

import sys
import os
from datetime import datetime
import time
import subprocess
import requests

try:
    if(len(sys.argv) < 5): 
        raise Exception("At least three arguments <mode>, <name>, <date> and <time> are neeeded!")
    apikey = os.environ['TRELLO_APIKEY']
    token = os.environ['TRELLO_TOKEN']
    memberid = os.environ['TRELLO_MEMBERID']
    mode = sys.argv[1]
    cardname = sys.argv[2]
    date = sys.argv[3]
    mytime = sys.argv[4]
    attachmenturl = sys.argv[5] if len(sys.argv) == 6 else None
    if(mode == "maintenance"):
        listid = os.environ['TRELLO_MAINTENANCE_LISTID']
    elif(mode == "appointment"):
        listid = os.environ['TRELLO_APPOINTMENTS_LISTID']
    elif(mode == "deadline"):
        listid = os.environ['TRELLO_DEADLINES_LISTID']
    else:
        raise Exception("%s is not a known mode!" % mode)

    mydatetime = "%s %s" % (date, mytime)
    isodate = subprocess.check_output(["date", "-Iseconds", "-d", mydatetime]).decode('utf-8').strip('\n')

    urlsource_qureyparam = "&urlSource=%s" % attachmenturl if attachmenturl else "";
    targeturl = "https://api.trello.com/1/cards?name=%s&due=%s&idList=%s&idMembers=%s&key=%s&token=%s%s" % (cardname, isodate, listid, memberid, apikey, token, urlsource_qureyparam)

    payload = {}
    headers={}

    response = requests.request("POST", targeturl, headers=headers, data = payload)

    print(response.text.encode('utf8'))

except Exception as err:
    print("Error happened: \n%s" % err)
  
