# WAP to compute the factorial of the given numbe

num = int(input("Enter a number: "))
fact = 1 
for i in range (1,num+1):
    fact *= i
print("The factorial of given number is :",fact)    
