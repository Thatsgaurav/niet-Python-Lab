# . What is lambda function? Write a lambda function to compute area of a
# triangle.
print("A lambda function is a single-line function declared with no name,\n"
      "which can have any number of arguments, but it can only have one \n"
      "expression. Such a function is capable of behaving similarly to a \n"
      "regular function declared using the Python's def keyword.")

import math


def Area_of_Triangle(a, b, c):
    Perimeter = a + b + c
    s = (a + b + c) / 2

    Area = math.sqrt((s * (s - a) * (s - b) * (s - c)))

    print("\n The Perimeter of Traiangle = %.2f" % Perimeter);
    print(" The Semi Perimeter of Traiangle = %.2f" % s);
    print(" The Area of a Triangle is %0.2f" % Area)


Area_of_Triangle(6, 7, 8)