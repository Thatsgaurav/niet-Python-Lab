# WAP to find the sum of odd and even numbers separately within a given range.

n = int(input("Enter number of terms "))
e = 0
o = 0
for i in range(1, n+1):
    if i % 2 == 0:
        e = e + i
    else:
        o = o + i
print("EVEN =", e)
print("ODD =", o)
