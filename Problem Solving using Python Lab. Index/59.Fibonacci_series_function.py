# WAP to display the Fibonacci series using user defined function.

def fibo_seri(n):  
   if n <= 1:  
       return n  
   else:  
       return(fibo_seri(n-1) + fibo_seri(n-2))  
nterms = int(input("How many terms? "))  
if nterms <= 0:  
   print("Plese enter a positive integer")  
else:  
   print("Fibonacci sequence:")  
   for i in range(nterms):  
       print(fibo_seri(i)) 