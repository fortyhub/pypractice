#!/usr/bin/env python
#将mongodb作为队列，完成一个客户端和服务端，服务端读取json文件中的数据存入mongodb，
#客户端循环读取mongodb中的数据，若有则打印并且删除mongodb中的这条数据，若没有，则循环监听直到mongodb有数据。

import pymongo
import json

myclient = pymongo.MongoClient("mongodb://localhost:27017")
mydb = myclient["pytest"]
mycol = mydb["jsonfile4"]

while True:
    result = mycol.find_one_and_delete({'age':{'$gt':0}})
    if result == None:
        pass
    else:
        print(result)