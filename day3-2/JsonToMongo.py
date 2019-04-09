#!/usr/bin/env python
#读取多个json文件并且存入mongodb文档，注意如果数据已有（以_id判断），则更新，若没有，则新增。

import pymongo
import json

myclient = pymongo.MongoClient("mongodb://localhost:27017")
mydb = myclient["pytest"]

dblist = myclient.list_database_names()
if "pytest" in dblist:
    print("数据库已存在！")

mycol = mydb["jsonfile"]
collist = mydb.list_collection_names()
if "jsonfile" in collist:
    print("集合已存在！")

with open("test1.json",encoding='utf-8') as f:
    data = json.load(f)
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
    mycol.remove({'_id':employee['_id']})
    print(result)
    print(result.inserted_id)