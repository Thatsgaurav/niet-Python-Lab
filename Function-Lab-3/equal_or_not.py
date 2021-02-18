# WAP to check whether the two numbers are equal or not. 

def equal_or_not(a,b):
    if(a==b):
        return 0
    if(a>b):
        return 1
    if(a<b):
        return -1
a = int(input("Enter value of a : "))
b = int(input("Enter value of b: "))
result = equal_or_not(a,b)
if (result==0):
    print("a is equal to b")
if (result==1):
    print("a is greater than b")
if (result==-1):
    print("a is less than b")        
        