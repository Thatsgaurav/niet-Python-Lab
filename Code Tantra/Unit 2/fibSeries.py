# WAP to compute the sum of Fibonacci series up to nth term.

n = int(input("Enter number of terms "))
a = 0
b = 1
s = a + b
for i in range(3, n+1):
    c = a + b
    s = s + c
    a = b
    b = c
print("Sum of Fibonacci series upto ", n, "th terms", s)
