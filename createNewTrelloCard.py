#!/usr/bin/env python3
# simple script without much effort in parsing the cl arguments because it will be called from bash wrapper functions

import sys
import os
from datetime import datetime
import time

try:
    print("hi");
    if(len(sys.argv) < 5): 
        raise Exception("At least three arguments <mode>, <name>, <date> and <time> are neeeded!")
    mode = sys.argv[1]
    cardname = sys.argv[2]
    date = sys.argv[3]
    mytime = sys.argv[4]
    attachmenturl = sys.argv[5] if len(sys.argv) == 6 else None
    if(mode == "maintenance"):
        listid = os.environ['TRELLO_MAINTENANCE_LISTID']
    elif(mode == "deadline"):
        listid = os.environ['TRELLO_APPOINTMENTS_LISTID']
    elif(mode == "appointment"):
        listid = os.environ['TRELLO_DEADLINES_LISTID']
    else:
        raise Exception("%s is not a known mode!" % mode)

    print(listid)
    print(cardname)
    print(date)
    print(mytime)
    print(attachmenturl)
    mydatetime = "%s %s:00.000000" % (date, mytime)
    duedate = datetime.strptime(mydatetime, '%Y%m%d %H:%M:%S.%f').isoformat()
    print(duedate)
    print(datetime.now().isoformat())

except Exception as err:
    print("Error happened: \n%s" % err)
  
