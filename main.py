import math
import matplotlib.pyplot as plt
import numpy


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


x0 = 1
fx = 3
delta = 0.1
rng = 1000
x_min = -2
x_max = 2
step = (x_max-x_min)/rng
x_values = []
fx_values = []
dxfx_values = []
gx_values = []

i = 0
while i < rng:
    x_values.append(x_min+i*step)
    i += 1

for n in x_values:
    fx_values.append(f(n, fx))

for n in x_values:
    dxfx_values.append(dxf(n, fx))

for n in x_values:
    gx_values.append(g(n, delta, fx))

print(f(x0, fx))
print(dxf(x0, fx))
plt.plot(
    numpy.array(x_values), numpy.array(fx_values), 'r',
    numpy.array(x_values), numpy.array(dxfx_values), 'y',
    numpy.array(x_values), numpy.array(gx_values)
)
# plt.ylabel('some numbers')
# plt.xlabel('Some other numbers')
plt.show()
