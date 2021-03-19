# WAP to check whether the given number is a prime number or not using user defined function.

def test_prime(n):
    if (n==1):
        return "not a prime number"
    elif (n==2):
        return "prime number"
    else:
        for x in range(2,n):
            if(n % x==0):
                return "not a prime number"
        return "prime number"

num = int(input("Enter any number :"))                     
print(test_prime(num))