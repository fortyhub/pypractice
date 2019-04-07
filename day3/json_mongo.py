#!/usr/bin/env python
# -*- coding:utf-8 -*-

import pymongo


myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["python"]
mycol = mydb['testjson']

dblist = myclient.list_database_names()
if "python" in dblist:
    print("数据库已存在！")

with open("test1.json",'r') as f:
    data = f.read()
with open("test2.json",'r') as f:
    data2 = f.read()
with open("test3.json",'r') as f:
    data3 = f.read()
    print data3

mylist = [
  { "_id": 1, "test1.json": data},
  { "_id": 2, "test2.json": data2},
  { "_id": 3, "test3.json": data3}
]

mycol.insert_many(mylist)

#报错啊bson.errors.InvalidDocument: key 'test1.json' must not contain '.'

for x in mycol.find():
    print(x)