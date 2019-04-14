#!/usr/bin/env python

#杨辉三角

#def triangles():
#    g = [1]
#    while True:
#        yield g[:len(g)]
#        g.append(0)
#        g = [g[i-1]+g[i] for i in range(len(g))]
#        print(g)
def triangles():
    s = [1]
    yield s
    n = len(s)
    while True:
        n = n+1
        i = 0
        l = [1]
        for m in s:
            if i==0:
                a = m
            else:
                l.append(a+m)
                a=m
            i = i+1
        l.append(1)
        s = l
        yield s

n = 0
results = []
for t in triangles():
    print(t)
    results.append(t)
    n = n + 1
    if n == 6:
        break
if results == [
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1],
    [1, 5, 10, 10, 5, 1]]:
    print('测试通过!')
else:
    print('测试失败!')