f1, f2 = input().split()
fn1 = open(f1, 'r')
fn2 = open(f2, 'r')
sentence = input().lower()
sen = ''
pos = 0
neg = 0
for i in sentence:
    if 'a' <= i <= 'z' or i == ' ':
        sen += i
sen = sen.split()

for i in fn1:
    n = i[:-1]
    for e in sen:
        if e == n:
            pos += 1
for i in fn2:
    n = i[:-1]
    for e in sen:
        if e == n:
            neg += 1            
            
total = len(sen)
neu = total - pos - neg
print(total, pos, neg, neu)

ans = pos - neg

if ans > 0:
    print(str(ans), 'Positive')
elif ans < 0:
    print(str(ans), 'Negative')
else:
    print(str(ans), 'Neutral')
