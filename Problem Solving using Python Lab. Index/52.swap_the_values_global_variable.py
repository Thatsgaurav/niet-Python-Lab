# WAP to swap the values of two variable that are defined as global variables

def swap(a, b):
    t = a
    a = b
    b = t
    return a, b
a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))
a, b = swap(a, b)
print("Swapped value of x is = %d & y is = %d" %(a,b))