# Python Program to Solve Quadratic Equation
0
import cmath
a = float(input("Enter first number:"))
b = float(input("Enter Second number:"))
c = float(input("Enter Third number:"))

d = (b**2) - (4*a*c)

s1 = (-b-cmath.sqrt(d))/(2*a)
s2 = (-b+cmath.sqrt(d))/(2*a)

print('The solution are {0} and {1}'.format(s1,s2))