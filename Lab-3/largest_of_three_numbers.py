# WAP to find the largest of three numbers using user defined function. 

num1 = int(input("Enter First number: "))
num2 = int(input("Enter Second number: "))
num3 = int(input("Enter Third number: "))

def largest_num():
    if(num1>=num2) and (num1>=num2):
        largest=num1
    elif(num2>=num1) and (num2>=num3):
        largest=num2
    else:
        largest=num3
    print("Largest number is",largest)
largest_num()            
