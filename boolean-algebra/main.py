# Basic Boolean operations

def AND(a, b):
    return a and b

def OR(a, b):
    return a or b

def NOT(a):
    return not a

def XOR(a, b):
    return a != b

# Test the operations
a, b = True, False
print(f"AND({a}, {b}) = {AND(a, b)}")
print(f"OR({a}, {b}) = {OR(a, b)}")
print(f"NOT({a}) = {NOT(a)}")
print(f"XOR({a}, {b}) = {XOR(a, b)}")

