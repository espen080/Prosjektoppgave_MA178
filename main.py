import math

import matplotlib.pyplot as plt


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


print(f(1, 2))
# plt.plot([1, 2, 3, 4], [2, 3, 2, 3])
# plt.ylabel('some numbers')
# plt.xlabel('Some other numbers')
# plt.show()
