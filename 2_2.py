import math

def fx(x,t):
    return (10 - (2 * math.cos(t) + 8.5 * math.cos(x)))**2 + (6 - (2 * math.sin(t) + 8.5 * math.sin(x)))**2 - 7**2


def dfdx(x,t):
    if t == 0:
        return 136 * math.sin(x) - 102 * math.cos(x)
    elif t == math.pi/2:
        return 170 * math.sin(x) - 68 * math.cos(x)
    elif t == math.pi:
        return 204 * math.sin(x) - 102 * math.cos(x)

         

def next_x(x,t):
    return x - (fx(x,t) / dfdx(x,t))


def getZeroPoint(i, ex,t):
    c = 0
    n = i
    while abs(fx(n,t)) > ex:
        if dfdx(n,t) == 0:
            n += 0.1
        if c > 100:
            n = i + 0.1
            c = 0
        n = next_x(n,t)
        c += 1
        #print(n)
    return n


Ex = 10 ** (-12)
i = 0
ts =[0,math.pi/2, math.pi]
for t in ts:
    print('Theta1 = {:.3f} '.format(t))
    for i in range(0,7):
        p = getZeroPoint(i, Ex, t)
        print('X0 = {:.1f} => Nullpunkt = {:.3f}'.format(i, p))


