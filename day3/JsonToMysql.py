#!/usr/bin/python
# -*- coding: UTF-8 -*-

import json
import MySQLdb

db = MySQLdb.connect("localhost","root","Aixocm123","testdb",charset='utf8')
with open("test1.json",'r') as f:
    data = json.loads(f.read())
    print data


f.close()
db.close()
