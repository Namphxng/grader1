import math

m , n = [int(e) for e in input().split()]
if m < n:
    a, b, c = [int(z) for z in input().split()]
    if m %2 != 0:
        u = v = w = k = 0
        while m > k:
            if a > b:
                if a + c >= k:
                    u += 3
                    v -= 2
                    w += 1
                else:
                    u -= 1
                    v += 2
                    w += 3
            else:
                b = (a+b)/2
            k += 1
        print(u, v, w)
    else:
        a, b = b, a
        a = c - (2*b)
        c = a**2
        b =( 3*c )+1
        print(a, b, c)
else:
    if m == n:
        s = int(input())
        i = k = s
        o = m-1
        for j in range(0,o):
            x = int(input())
            if x < i:
                i = x
            if x > k:
                k = x
        print(i*k)
    else:
        if (m+n)%3 == 0:
            r = math.sqrt(m) + (n**(1/3))
        else:
            r = math.sin((m*math.pi)/(m+n)) + math.cos((n*math.pi)/(m+n))
        print(round(r, 2))