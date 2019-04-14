#!/usr/bin/env python

# 你的衣服加工厂需要生产20000件衣服待卖出，我找你第一次拿一件衣服，
# 第二次拿一件衣服，第三次拿5件衣服。打印出你的工厂如果再有顾客来
# 是从你工厂最开始生产的第几件衣服拿起的？

import sys

n=0

def create_counter(b):
    def increase():
        global n
        n = n+b
        while n<20000:
            yield n
        return 'count gt 20000'

    it = increase()

    def counter():
        return next(it)

    return counter()

while True:
    try:
        g = create_counter(int(input("请输入本次取衣服件数: ")))
        print(g)
    except StopIteration as e:
        print("生成器返回值：",e.value)
        break