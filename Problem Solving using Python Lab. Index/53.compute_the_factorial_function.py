# WAP to compute the factorial of the given number using user defined function

def factorial(num):
    fact=1
    for i in range(1, num+1):
        fact=fact*i
    return fact     
num=int(input("Please enter any number to find factorial: "))
result=factorial(num)
print("The factorial of %d = %d"%(num,result))