# WAP to compute the sum of the first n natural number using recursion.

def recurSum(n): 
    if n <= 1: 
        return n 
    return n + recurSum(n - 1) 
n = int(input("Enter any number :"))
print("sum of given number is:",recurSum(n))