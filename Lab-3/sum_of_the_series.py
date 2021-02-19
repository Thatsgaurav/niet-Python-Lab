# WAP compute the sum of the series using user defined function. 

def fact(n):
    f = 1 
    if(n==0 or n==1):
        return 1 
    else:
        for i in range(1,int(n+1)):
            f = f*i
    return f
n = int(input("Enter the value of n: "))
s = 0.0
for i in range(1,n+1):
    s = s+(float(i**i)/fact(i))
print("Result :",s)                      