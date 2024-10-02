import math

n = input().split()
if len(n) != 2:
    print('Error!')
else:
    v0, degree = map(float, n)
    degree = math.radians(degree)

    h = ((v0**2)*(math.sin(degree)**2))/(2*9.81)

    r = ((v0**2)*(math.sin(degree*2)))/(9.81)

    t = abs((2*v0*math.sin(degree))/(9.81))

    rounding1 = f'{round(h,2):.2f}'
    rounding2 = f'{round(r,2):.2f}'
    rounding3 = f'{round(t,2):.2f}'
    print(str(rounding1), str(rounding2), str(rounding3))