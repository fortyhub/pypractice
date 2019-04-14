#!/usr/bin/env python

#用生成器实现监听文件的新输入末尾行(tail -f)

import subprocess

def tail():
    while True:
        line = subprocess.Popen("tail -f test.txt",shell=True)
        if line:
            yield line

g = tail()

while True:
    print(next(g))
