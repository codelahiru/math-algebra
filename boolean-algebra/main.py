# ------------- 1. Basic Boolean operations -------------

def AND(a, b):
    return a and b

def OR(a, b):
    return a or b

def NOT(a):
    return not a

def XOR(a, b):
    return a != b

# Test the operations
# a, b = True, False
# print(f"AND({a}, {b}) = {AND(a, b)}")
# print(f"OR({a}, {b}) = {OR(a, b)}")
# print(f"NOT({a}) = {NOT(a)}")
# print(f"XOR({a}, {b}) = {XOR(a, b)}")

# 2. ----------------- Generate a truth table for a given Boolean function -------------

def truth_table(func):
    for a in [False, True]:
        for b in [False, True]:
            result = func(a, b)
            print(f"{a} {b} | {result}")

# Define a Boolean function (example: (A AND B) OR (NOT A AND NOT B))
def boolean_func(a, b):
    return (a and b) or (not a and not b)

# Generate the truth table
print("A B | Result")
truth_table(boolean_func)

#. ------------------- Boolean Expression Simplification (using sympy) ------------------

from sympy.logic.boolalg import Or, And, Not
from sympy.abc import A, B, C

# Define a Boolean expression
expr = Or(And(A, B), And(Not(A), Not(B)))

# Simplify the Boolean expression
simplified_expr = expr.simplify()
print(f"Simplified expression: {simplified_expr}")

# 4. -------------- Logic Gates Simulation ----------------------

# Define logic gates as functions

def AND(a, b):
    return a and b

def OR(a, b):
    return a or b

def NOT(a):
    return not a

def NAND(a, b):
    return not (a and b)

def NOR(a, b):
    return not (a or b)

def XOR(a, b):
    return a != b

def XNOR(a, b):
    return not (a != b)

# Simulate a complex circuit (example: (A AND B) OR (A NAND B))
def complex_circuit(a, b):
    return OR(AND(a, b), NAND(a, b))

# Test the complex circuit
a, b = True, False
print(f"Complex circuit result for A={a}, B={b}: {complex_circuit(a, b)}")





