# WAP to display all the prime numbers in given range.

a = int(input("Enter first number "))
b = int(input("Enter last number "))

print("Prime numbers from ", a, "to", b, "are")
for i in range(a, b+1):
    flag = 0
    for j in range(2, i//2+1):
        if i % j == 0:
            flag = 1
            break
    if flag == 0:
        print(i, end=' ')
    if i == 4:
        print(4, end=' ')
