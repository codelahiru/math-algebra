import sympy
from sympy import symbols
from sympy import *

a = sympy.sqrt(8)
print(a)

x, y = symbols('x y')
expr = x + 2*y
print(expr)

x, y = symbols('x y')
expr = (x + 2*y)*y
print(expr)

expr + 1
print(expr + 1)

a = integrate(sin(x**2), (x, -oo, oo))
print(a)








