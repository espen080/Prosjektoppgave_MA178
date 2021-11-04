import math

def nextX(x):
    return x - (fx(x)/dfdx(x))

def fx(x):
    return 3*x**2 + 4*x - 4


def dfdx(x):
    return 6*x + 4


def getZeroPoint(i,ex):
    c=0
    n = i
    while(abs(fx(n))>ex):
        if(dfdx(n)== 0):
            n+=0.1
        if(c>100):
            n = i + 0.1
            c = 0
        n=nextX(n)
        c+=1
    return n

Ex = 10**(-12)
r = -3
i = r
while(i<-r):
    p = getZeroPoint(i,Ex)
    print('X0 = {:.1f} => Nullpunkt = {:.3f}'.format(i,p))
    i +=0.1