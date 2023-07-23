from matplotlib import pyplot

import numpy
import math

a = -10000
b = 10000

def my_func(x):
    return x + 4

max_inter = 25
p_med = 0
erro = 10000

for i in range(max_inter):
    p_med = (a + b)/2
    erro = b - p_med
    f_p = my_func(p_med)
    if f_p > 0:
        b = p_med
    else:
        a = p_med

print(str(p_med))

