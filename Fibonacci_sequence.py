# Python Program to Print the Fibonacci sequence

n = int(input("Enter number terms: "))
n1, n2 = 0, 1
count = 0
if n <= 0:
   print()
elif n == 1:
   print("Fibonacci sequence ",n,":")
   print(n1)
else:
   print("Fibonacci sequence:")
   while count < n:
       print(n1)
       nth = n1 + n2
       n1 = n2
       n2 = nth
       count += 1