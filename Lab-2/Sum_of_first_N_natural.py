# Python Program to Find the Sum of first N natural numbers

num = int(input("Enter Number: "))

if num < 0:
    print()
else:
    sum = 0
    while(num > 0):
        sum += num 
        num -= 1
    print("sum is", sum)