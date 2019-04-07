#!/usr/bin/python
# -*- coding: UTF-8 -*-

import MySQLdb

#打开数据库
db = MySQLdb.connect("localhost","root","Aixocm123","testdb",charset='utf8')

#使用cursor()方法获取操作游标
cursor = db.cursor()

cursor.execute("select version()")

data = cursor.fetchone()

print("Database version : %s" %(data))

db.close()