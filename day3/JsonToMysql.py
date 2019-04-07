#!/usr/bin/python
# -*- coding: UTF-8 -*-

import json
import MySQLdb

db = MySQLdb.connect("localhost","root","Aixocm123","testdb",charset='utf8')
with open("employee.json",'r') as f:
    data = json.load(f)
    print data


f.close()
db.close()
