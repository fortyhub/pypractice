#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys
import MySQLdb

db = MySQLdb.connect("localhost","root","Aixocm123","testdb",charset='utf8')
cursor = db.cursor()

sql = "select * from testuser limit %d " %(int(sys.argv[1])*int(sys.argv[2]))

try:
    cursor.execute(sql)
    results = cursor.fetchall()
except:
   print "Error: unable to fecth data"

print results

