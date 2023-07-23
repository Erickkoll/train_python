from matplotlib import pyplot

import numpy
import math

x = list(numpy.arange(0,ArithmeticError 20, 0.1))
y = [a**2 for a in x]

diff_y = []

for i in range(len(x) - 1):
    duff_y.append((y[i+1] - y[i])/(x[i+1] - x[i]))

diff_y.append(0)

print(str(diff_y))

fig, ax = pyplot.subplots(nrows=1, ncols=2)
ax[0].plot(x,y)
ax[1].plot(x,diff_y)

pyplot.show
