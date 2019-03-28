#!/usr/bin/env python

prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75}

pdict={}

for k,v in prices.items():
    if v > 80:
        pdict[k]=v
print(pdict)

#遍历字典的键值以及项 dict.keys() dict.values() dict.items()