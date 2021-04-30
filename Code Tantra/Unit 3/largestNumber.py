# WAP to find the largest of three numbers using user defined function.

num1 = int(input("Enter First Number "))
num2 = int(input("Enter Second Number "))
num3 = int(input("Enter Third Number "))


def largest_Number():
    if(num1 > num2):
        if(num1 > num3):
            largest = num1
        else:
            largest = num3
    else:
        if num2 > num3:
            largest = num2
        else:
            largest = num3
    print("Largest number =", largest)


largest_Number()
