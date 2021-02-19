# Python Program to Find the Factors of a Number

def print_factors(x):
   print("factors of",x,"are:")
   for i in range(1, x + 1):
       if x % i == 0:
           print(i)

num = int(input("Enter number: "))

print_factors(num)


# NIET GREATER NOIDA LAB 2 --->>> Completed Hear!!! -----<<<<