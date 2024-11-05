def add(list):
    ans = 0
    for i in list:
        ans += i
    return ans

num = [float(e) for e in input().split()]
time = int(input())
total = []
l = []
ans = []
last = num[-1]
for i in range(len(num)):
    num = num[:-1]
    num.insert(0, last)
    l.append(num)
    last = num[-1]
    s = add(num[:time])
    total.append(s)

m = max(total)

for i in range(len(total)):
    if total[i] == m:
        ans = l[i][:time]
        
print(round(m, 2))        
print(ans)
