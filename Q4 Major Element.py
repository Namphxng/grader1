set = [int(e) for e in input().split()]
set.sort()
c = 1
count, num = [], []
for i in range(len(set)-1):
    if set[i] == set[i + 1]:
        c += 1
    else:
        count.append(c)
        num.append(set[i])
        c = 1
count.append(c)
num.append(set[-1])
n = max(count)
if n < len(set)//2 or len(count) == 2 and n == len(set)//2:
    print(-1)
else:
    print(num[count.index(n)])