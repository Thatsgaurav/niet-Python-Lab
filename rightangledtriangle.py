# Python program to calculate the hypotenuse of a right angled triangle. 

import math

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

result = math.sqrt((a ** 2) + (b ** 2))
print("Hypotenuse:", result)