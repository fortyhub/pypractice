#!/usr/bin/env python
# -*- coding:utf-8 -*-

import redis
import sys

r = redis.Redis(host='localhost',port=6379,db=0)
with open(sys.argv[1],'r') as f:
    data = f.read()
    print data
    print sys.argv[1]

r.rpush("testjson",data)

print r.llen("testjson")
print r.lrange("testjson",0,-1)
