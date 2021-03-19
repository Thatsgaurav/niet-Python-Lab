# WAP to find the largest of three numbers using user defined function

def find_largest():      #function definition
     if(num1>=num2) and (num1>=num2):
         largest=num1
     elif(num2>=num1) and (num2>=num3):
         largest=num2
     else:
         largest=num3
     print("Largest number is",largest)

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the Third number: "))

find_largest()