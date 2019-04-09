#!/usr/bin/env python
#如果不要mongodb自带的_id，自己生成不是object对象的id？将1题中的数据，以自己生成的id作为索引，而没有object对象的id。

import pymongo
import json
import time


myclient = pymongo.MongoClient("mongodb://localhost:27017")
mydb = myclient["pytest"]

dblist = myclient.list_database_names()
if "pytest" in dblist:
    print("数据库已存在！")

mycol = mydb["jsonfile2"]
collist = mydb.list_collection_names()
if "jsonfile" in collist:
    print("集合已存在！")

with open("test2.json",encoding='utf-8') as f:
    data = json.load(f)
    print(data)

data['id'] = int(round(time.time()*1000))
print(data)

condition = {'first_name':data['first_name'],'last_name':data['last_name']}
employee = mycol.find_one(condition)
print(employee)
if employee == None:
    result = mycol.insert_one(data)
    print(result)
    print(result.inserted_id)
else:
    result = mycol.insert_one(data)
    mycol.remove({'id':employee['id']})
    print(result)
    print(result.inserted_id)