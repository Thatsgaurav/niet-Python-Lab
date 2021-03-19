# WAP to display all the prime numbers from 1 to n. 

num1 = int(input("Enter any number :"))
nterm = int(input("Enter any number :"))

print("Prime numbers between", num1, "and", nterm, "are:")
for num in range(num1, nterm + 1):
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)