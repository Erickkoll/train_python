from sympy import *

x, y, z, s = symbols('x y z s')
init_printing(use_unicode=True)

a = 30 * cos(x) + 2 * x ** 2

print(diff(a,x))
print(integrate(a,x))

#plot(a,(x,-20, 20))
#plot(diff(a))
#plot(integrate(a,x))

b = laplace_transform(a,x,s)
print(laplace_transform(a,x,s))
plot(b[0],(s, -0.005, 0.005))
