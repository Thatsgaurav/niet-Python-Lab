# WAP to compute the sum of Fibonacci series up to nth term using user defined function.

def fibo(n):
    if n<2:
        return 1
    else:
        res = fibo(n-1) + fibo(n-2)
        return res

num = int(input("Enter any number:"))
sum = 0
for i in range(0, num):
    r = fibo(i)
    sum += r
    print(r)

print("Sum is:", sum)