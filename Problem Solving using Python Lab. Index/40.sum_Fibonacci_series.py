# WAP to compute the sum Fibonacci series up to nth term.

def fibo(n):
    if n<2:
        return 1
    else:
        res = fibo(n-1) + fibo(n-2)
        return res

n= int(input("Enetr number :"))
sum = 0
for i in range(0, n):
    r = fibo(i)
    sum += r
    print(r)

print("Suma", sum)