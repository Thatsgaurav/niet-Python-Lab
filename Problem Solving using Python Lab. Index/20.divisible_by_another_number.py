# WAP to check whether a number is divisible by another number

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
remainder = num1 % num2
if remainder == 0:
    print(num1,"is divisible by",num2)
else:
    print(num1,"is not divisible by", num2)