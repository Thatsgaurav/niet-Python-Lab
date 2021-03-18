#  Python program to calculate the hypotenuse of a right-angled triangle.
# (h=(b*b +h*h)**0.5) 

import math

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

result = math.sqrt((a ** 2) + (b ** 2))
print("Hypotenuse:", result)