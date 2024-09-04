import sympy
from sympy import symbols
from sympy import *

b = sympy.sqrt(3)
print(b)

x, t, z, nu = symbols('x t z nu')
init_printing(use_unicode=True)

y = diff(sin(x)*exp(x), x)
print(y)

t = integrate(exp(x)*sin(x) + exp(x)*cos(x), x)
print(t)

k = integrate(sin(x**2), (x, -oo, oo))
print(k)

k2 = limit(sin(x)/x, x, 0)
print(k2)