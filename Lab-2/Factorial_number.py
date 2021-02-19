# Python Program to Find the Factorial of a given number

num = int(input("Enter a number: "))
factorial = 1
if num < 0:
   print()
elif num == 0:
   print()
else:
   for i in range(1,num + 1):
       factorial = factorial*i
   print("factorial of",num,"is",factorial)