import math
import matplotlib.pyplot as plt
import numpy


class Func:
    def __init__(self, num, x0, delta, x_min, x_max):
        self.num = num
        self.x0 = x0
        self.delta = delta
        self.x_min = x_min
        self.x_max = x_max
        self.rng = 1000
        self.step = (x_max-x_min)/self.rng
        self.x_values = get_x_values(self.step, self.rng, self.x_min)
        self.fx_values = get_fx_values(self.x_values, self.num, 'fx', self.delta)
        self.dxfx_values = get_fx_values(self.x_values, self.num, 'dxfx', self.delta)
        self.gx_values = get_fx_values(self.x_values, self.num, 'gx', self.delta)
        self.ex_values = get_fx_values(self.x_values, self.num, 'ex', self.delta)


def get_x_values(step, rng, x_min):
    i = 0
    x_values = []
    while i < rng:
        x_values.append(x_min+i*step)
        i += 1
    return numpy.array(x_values)


def get_fx_values(x_values, num, func, delta):
    values = []
    match func:
        case 'fx':
            for n in x_values:
                values.append(f(n, num))
        case 'dxfx':
            for n in x_values:
                values.append(dxf(n, num))
        case 'gx':
            for n in x_values:
                values.append(g(n, delta, num))
        case 'ex':
            for n in x_values:
                values.append(e(n, delta, num))
        case _:
            raise ValueError('Unexpected input, accepted func values are: [fx, dxfx, gx, ex]')
    return numpy.array(values)


def f(x, o):
    match o:
        case 1:
            return 7*(x**2)-(8*x)+1
        case 2:
            return math.sin(x)
        case 3:
            return (1-x)/(x+3)**2
        case 4:
            return math.sqrt(1+x**2)
        case _:
            raise ValueError('Unexpected input, accepted o values are [1-4]')


def dxf(x, o):
    match o:
        case 1:
            return 14*x-8
        case 2:
            return math.cos(x)
        case 3:
            return (x-5)/(x+3)**3
        case 4:
            return x/math.sqrt(1+x**2)
        case _:
            raise ValueError('Unexpected input, accepted o values are [1-4]')


def g(x, d, o):
    return (f(x+d, o)-f(x, o))/d


def e(x, d, o):
    return math.fabs(dxf(x, o)-g(x, d, o))

delt = float(input('Select function delta: '))

funcs = [Func(1, 1, delt, 0, 2),
         Func(2, math.pi/4, delt, 0, 2+math.pi),
         Func(3, 1, delt, -2, 2),
         Func(4, 5, delt, 0, 10)]

for f in funcs:
    plt.figure(f.num)
    plt.plot(f.x_values, f.fx_values, 'r-', label='f(x)')
    plt.plot(f.x_values, f.dxfx_values, 'y-', label='f\'(x)')
    plt.plot(f.x_values, f.gx_values, 'b--', label='g(x)')
    plt.plot(f.x_values, f.ex_values, 'g--', label='e(x)')
    plt.grid()
    plt.legend()
    #plt.figure(str(f.num)+' e')
    #plt.plot(f.x_values, f.ex_values, 'g--', label='e(x)')
    #plt.legend()
    #plt.grid()

for f in funcs:
    plt.figure('Figure '+str(f.num)+' E(x)')
    #plt.plot(f.x_values, f.fx_values, 'r-', label='f(x)')
    #plt.plot(f.x_values, f.dxfx_values, 'y-', label='f\'(x)')
    #plt.plot(f.x_values, f.gx_values, 'b--', label='g(x)')
    plt.plot(f.x_values, f.ex_values, 'g--', label='e(x)')
    plt.grid()
    plt.legend()

plt.show()
