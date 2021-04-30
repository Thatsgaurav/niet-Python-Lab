# WAP to compute the sum of factorial of the first n natural number.

B = 0
A = 1

m = int(input("Enter number of terms "))
for k in range(1, m+1):
    A = 1
    for i in range(1, k+1):
        A = i * A
    B = B + A
print("Sum of series =", B)
