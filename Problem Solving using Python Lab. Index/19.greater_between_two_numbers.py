# WAP to find greater between two numbers

num1=int(input("Enter your first number:"))
num2=int(input("Enter your second number: "))
if(num1>num2):
    print("{} is greater".format(num1))
elif(num2>num1):
    print("{} is greater".format(num2))
else:
    print("{} and {} are equal".format(num1,num2))