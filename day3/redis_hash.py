#!/usr/bin/env python
# -*- coding:utf-8 -*-

import redis
import sys

r = redis.Redis(host='localhost',port=6379,db=0)
with open(sys.argv[1],'r') as f:
    data = f.read()
    print data
    print sys.argv[1]

r.hset("testhash",sys.argv[1],data)
print r.hgetall("testhash")