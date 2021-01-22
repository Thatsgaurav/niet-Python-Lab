# Python program to calculate the hypotenuse of a right angled triangle. 

import math

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

result = math.sqrt((a ** 2) + (b ** 2))
print("Hypotenuse:", result)

# Another Type 
# import math

# def main():
#     side1 = int(input("Enter side1 :"))
#     side2 = int(input("Enter side2 :"))
#     hypotenuse = math.sqrt(math.pow(side1, 2)+math.pow(side2, 2))
#     print("HYPOTENUSE = "+ str(hypotenuse))
    
    
# if __name__ == '__main__':
#     main()