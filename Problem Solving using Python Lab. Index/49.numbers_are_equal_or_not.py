# WAP to check whether the two numbers are equal or not.

def equal(a,b):
    if a==b:
        return a, "is equal to", b
    else:
        return a, "is not equal to", b

num1 = int(input("Enter the second number: "))
num2 = int(input("Enter the second number: "))     

print(equal(num1,num2))