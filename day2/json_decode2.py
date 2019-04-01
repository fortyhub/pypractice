#!/usr/bin/env python

import json
import sys

data=[]
with open('aim2.json','w') as f:
    f1=open('origin1.json',encoding='utf-8')
    data1=json.load(f1)
    data.append(data1)
    print(data)
    f1.close()
    f2=open('origin2.json',encoding='utf-8')
    data2=json.load(f2)
    data.append(data2)
    print(data)
    json.dump(data,f)
    f2.close()
    text=json.load(f)
    print(text)