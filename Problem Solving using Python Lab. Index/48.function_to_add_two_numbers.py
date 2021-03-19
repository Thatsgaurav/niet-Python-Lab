# WAP to implement the user defined function to add two numbers

def add_numbers(x,y):
   sum = x + y
   return sum

num1 = int(input("Enter first number :"))
num2 = int(input("Enter second number :"))

print("The sum is", add_numbers(num1, num2))