from matplotlib import pyplot
import math

x = list(range(-700,700))
y = [(4*math.cos(a) + math.pow(a,2)) for a in x]

pyplot.plot(x,y,'r--')
pyplot.show()

