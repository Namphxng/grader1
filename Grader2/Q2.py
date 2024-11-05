def parse_boxing_match(result):
    sc = result.split()
    sc = sc[1:]
    half = len(sc)//2
    x = sc[:half]
    y = sc[half:]
    if result[0] == 'R':
        r = x
        b = y
    elif result[0] == 'B':
        r = y
        b = x
    ans = []
    r = list(map(int, r))
    b = list(map(int, b))
    ans.append(r)
    ans.append(b)
    return ans

def calculate_round_points(rk, bk):
    round = len(rk)
    r = [10]*round
    b = [10]*round
    for i in range(round):
        r[i] = r[i] - rk[i]
        b[i] = b[i] - bk[i]
    print(r)
    print(b)
    return ' '



def add(list):
    ans = 0
    for i in list:
        ans += i
    return ans



def show_match_result(rp, bp):
    match = len(rp)
    ans = ''
    for i in range(match):
        if rp[i] > bp[i]:
            ans += 'R'
        elif rp[i] < bp[i]:
            ans += 'B'
        else:
            ans += 'T'
    print(ans)
    result = ''
    result += str(add(rp))
    result += ' '
    result += str(add(bp))
    print(result)
    if add(rp) > add(bp):
        print('Red')
    elif add(rp) < add(bp):
        print('Blue')
    else:
        print('Draw')
    
exec(input().strip())
