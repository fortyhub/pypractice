#!/usr/bin/env python
#将mongodb作为队列，完成一个客户端和服务端，服务端读取json文件中的数据存入mongodb，
#客户端循环读取mongodb中的数据，若有则打印并且删除mongodb中的这条数据，若没有，则循环监听直到mongodb有数据。

import pymongo
import json
import sys

myclient = pymongo.MongoClient("mongodb://localhost:27017")
mydb = myclient["pytest"]
mycol = mydb["jsonfile4"]

with open(sys.argv[1],encoding='utf-8') as f:
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