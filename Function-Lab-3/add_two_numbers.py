# WAP to implement the user defined function to add two numbers. 

def add_num(a,b):
    sum=a+b
    return sum
num1=int(input("Enter First number: "))
num2=int(input("Enter Second number: "))

print("sum is",add_num(num1,num2))