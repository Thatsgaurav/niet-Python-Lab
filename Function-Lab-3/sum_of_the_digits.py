# WAP to compute the sum of the digits using user defined function. 

def getSum(n):  
     
    sum = 0
    for digit in str(n):   
      sum += int(digit)        
    return sum
    
n = int(input("Enter numbers: "))
print(getSum(n))
