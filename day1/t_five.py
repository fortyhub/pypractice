#!/usr/bin/env python

import re

filename = 'a.c'
url = 'https://www.baidu.com'

print(filename.endswith('.c'))
print(filename.startswith('a.'))

print(url.startswith('https:'))

#有多个元素需要匹配的话  可以放入list中[ 'Makefile', 'foo.c', 'bar.py', 'spam.c', 'spam.h' ]

print(filename[-2:] == '.c')

print(re.match('https:',url))