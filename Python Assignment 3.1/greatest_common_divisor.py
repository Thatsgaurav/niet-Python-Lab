# Write a Python program to find the greatest common divisor(gcd) of two
# integers.

def gcd(x,y):
    rem = x%y
    if(rem==0):
        return y
    else:
        return gcd(y,rem)

n = int(input("Enter first number : "))
m = int(input("Enter second number : "))
print("The GCD of number is", gcd(n,m))