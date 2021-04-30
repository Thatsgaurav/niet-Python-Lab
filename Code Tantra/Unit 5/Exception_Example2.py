# Write a simple try except block.

# Take two integers num1 and num2 as input from the console using input() function. In try block divide num1 and num2. If there is no exception print the result as shown in Sample Input and Output 1, if there is an exception, handle that exception using except block by printing the error message as shown in the Sample Input and Output 2

# Sample Input and Output 1:
# Enter num1: 23
# Enter num2: 2
# Succesful Division, value of num1/num2  11.5

# Sample Input and Output 2:
# Enter num1: 56
# Enter num2: 0
# Exception occured

a = int(input("Enter num1: "))
b = int(input("Enter num2: "))
try:
    print("Succesful Division, value of num1/num2 ", a/b)
except ZeroDivisionError:
    print("Succesful occured")
