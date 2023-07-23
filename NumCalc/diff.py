from matplotlib import pyplot
import math
import numpy

x = list(numpy.arange(-20,20,0.1))
a = [a**2 for a in x]
#print(str(x(2)))
dx_dy = [(((dx_dy+0.5)**2 - dx_dy**2)//0.5) for dx_dy in x]

pyplot.plot(x, dx_dy)
pyplot.show()
