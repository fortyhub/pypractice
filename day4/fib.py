#!/usr/bin/env python

def fib(max):
    a,b,n = 0,1,0
    while n < max:
        yield b
        a,b = b,a+b
        n = n+1
    return 'done'

g = fib(10)

while True:
    try:
        x = next(g)
        print('generrator: ',x)
    except StopIteration as e:
        print("生成器返回值：",e.value)
        break