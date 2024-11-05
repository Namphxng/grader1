import math
n = int(input())
d = {}
for i in range(n):
    n1 = int(input())
    for i in range(n1):
        name, p = input().split()
        if name in d:
            d[name] += int(p)
        else:
            d[name] = int(p)
l = []
for i in d:
    k = [-d[i], i]
    l.append(k)
l = sorted(l)
for list in l:
    print(list[1], abs(list[0]))
    
