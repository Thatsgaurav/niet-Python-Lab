# Write a Python program to solve the Fibonacci sequence using recursion

def fibo(n):
    if n<2:
        return 1
    else:
        res = fibo(n-1) + fibo(n-2)
    return res

n= int(input("Enter any number : "))
sum = 0
for i in range(0, n):
    r = fibo(i)
    sum += r
    print(r)

print("Suma", sum)



# def recur_fibonacci(n):
#    if n <= 1:
#        return n
#    else:
#        return(recur_fibonacci(n - 1) + recur_fibonacci(n - 2))
#
# nterms = int(input("How many terms? "))
#
# if nterms <= 0:
#    print("Please enter a positive integer!")
# else:
#    print("Fibonacci sequence:")
#    for i in range(nterms):
#        print(recur_fibonacci(i))
