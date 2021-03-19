# WAP to compute the sum of digits of the given number using recursion

def sum_of_digit( n ): 
    if n == 0: 
        return 0
    return (n % 10 + sum_of_digit(int(n / 10))) 
num = int(input("Enter numbers: "))
result = sum_of_digit(num) 
print("Sum of digits in",num,"is", result) 