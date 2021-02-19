# Python program to check whether a number is prime number or not

num = int(input("Enter a number: "))
if num > 1:
   for i in range(2,num):
       if (num % i) == 0:
           print(num,"not prime number")
           break
   else:
       print(num,"prime number")
else:
   print(num,"not prime number")