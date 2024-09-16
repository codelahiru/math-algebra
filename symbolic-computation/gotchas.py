from sympy import *

x = symbols('x')
k1 = x + 1
print(k1)

a, b = symbols('b a')
k2 = x + a
print(k2)

x = symbols('x')
expr = x + 1
x = 2
print(expr)

x2 = symbols('x2')
expr = x2 + 1
x2 = 2
print(expr)

x + 1 == 4

x3 = Eq(x + 1, 4)
print(x3)

