w1, w2, w3, w4 = [e for e in input().lower().split()]
w1 = list(w1[::-1])
w2 = list(w2[::-1])
w3 = list(w3[::-1])
w4 = list(w4[::-1])

w1[0] = w1[0].upper()
w2[0] = w2[0].upper()
w3[0] = w3[0].upper()
w4[0] = w4[0].upper()
print(str(''.join(w1)), str(''.join(w2)), str(''.join(w3)), str(''.join(w4)))