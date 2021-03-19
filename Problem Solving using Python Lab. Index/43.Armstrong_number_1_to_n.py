# WAP to display all the Armstrong number from 1 to n.

num1 = int(input("Enter any number :"))
nterm = int(input("Enter any number :"))

for num in range(num1, nterm + 1):

   # order of number
   order = len(str(num))
    
   # initialize sum
   sum = 0

   temp = num
   while temp > 0:
       digit = temp % 10
       sum += digit ** order
       temp //= 10

   if num == sum:
       print(num)