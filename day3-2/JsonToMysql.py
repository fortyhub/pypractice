#!/usr/bin/env python

import pymysql
import json

con = pymysql.connect(host='localhost',port=3306,user='root',passwd='Aixocm123',db='testdb')
cursor = con.cursor()
with open('test1.json',encoding='utf-8') as f:
    data = json.load(f)
    print(data)

sql = "insert into employee(first_name,last_name,age,sex,income) value('%s','%s',%s,'%s',%s)" % \
      (data['first_name'],data['last_name'],data['age'],data['sex'],data['income'])

try:
    cursor.execute(sql)
    con.commit()
except:
    con.rollback()
cursor.close()