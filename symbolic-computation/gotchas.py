from sympy import *

x = symbols('x')
k1 = x + 1 + 34
print(k1)

a, b = symbols('b a')
k2 = x + a + b
print(k2)

x = symbols('x')
expr = x + 1 + a
x = 2
print(expr)

x2 = symbols('x2')
expr = x2 + 1
x2 = 2
print(expr)

x + 1 == 4

x3 = Eq(x + 1, 4)
print(x3)

x4 = Eq(x + 1, 4)
print(x4)

a = (x + 1)**2

x5 = (x + 1)**2 == x**2 + 2*x + 1
print(x5)

a = (x + 1)**2
b = x**2 + 2*x + 1 + 334
x6 = simplify(a - b)
print(x6)

x7, y7 = symbols('x7 y7')
k1 = x + 1 + y7
print(k1)

c = x**2 - 2*x + 1
a = cos(x)**2 - sin(x)**2
simplify(a - c)

a = cos(x)**2 - sin(x)**2
b = cos(2*x)
a.equals(b)

type(Integer(1) + 1)

k2 = Integer(1)/Integer(3)
print(k2)

x, y, z = symbols('x y z')
init_printing(use_unicode=True)
d0 = diff(cos(x), x)
print(d0)