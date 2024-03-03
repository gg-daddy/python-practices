import math


print(type(1 + 2))
print(type(2 / 4))

print(2 ** 4)
print(6 // 4)
print(6 % 4)

# List all math functions
math_functions = [name for name in dir(math) if callable(getattr(math, name))]

# Print the function names and their use cases
for function_name in math_functions:
    print(function_name)        



b = bin(1024)
print(b)
print(int(b,2))

h = hex(255)
print(h)
print(int(h, 16))

o = oct(255)
print(o)
print(int(o, 8))