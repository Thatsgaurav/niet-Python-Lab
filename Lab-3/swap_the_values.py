# WAP to swap the values of two variable that are defined as global variables. 

def swap(x,y):
    x = x + y 
    y = x - y
    x = x - y
    print("x after swap = ", x)
    print("y after swap = ", y)
x = int(input("Enter value of x: "))
y = int(input("Enter value of y: "))
swap(x,y)


# Working on this 