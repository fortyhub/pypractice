#!/usr/bin/env python
# -*- coding:utf-8 -*-

import redis
import sys

r = redis.Redis(host='localhost',port=6379,db=0)
ps = r.pubsub()
ps.subscribe('pubjson')
for item in ps.listen():
    if item['type'] == 'message':
        print item
        print item['channel']
        print item['data']