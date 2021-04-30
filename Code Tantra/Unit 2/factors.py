# WAP to display all the factors of a number.

def print_factors(x):
    print("Factors from 1 to", x, "are")
    for i in range(1, x + 1):
        if x % i == 0:
            print(i, end=" ")


num = int(input("Enter number "))
print_factors(num)
