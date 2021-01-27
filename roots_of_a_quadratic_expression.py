# Python program to find the roots of a quadratic expression

import cmath 

a = float(input("Enter first number: "))
b = float(input("Enter first number: "))
c = float(input("Enter first number: "))

d = (b**2) - (4*a*c)

sol1 = (-b-cmath.sqrt(d))/(2*a)
sol2 = (-b+cmath.sqrt(d))/(2*a)

print('solution is {0} and {1}'.format(sol1,sol2))

# The math module supplies mathematical functions on floating-point numbers
# the cmath module supplies equivalent functions on complex numbers.