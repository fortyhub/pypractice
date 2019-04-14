
g = [1]
g = [g[i-1]+g[i] for i in range(1)]
print(g)