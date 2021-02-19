# WAP to compute the HCF and LCM of two numbers using user defined function. 

# HCF
  
def hcfnaive(a,b): 
	if(b==0): 
		return a 
	else: 
		return hcfnaive(b,a%b) 

a = int(input("Enter value a: "))
b= int(input("Enter value b: "))
 
print ("The hcf of a and b is : ",end="") 
print (hcfnaive(a,b)) 

hcfnaive(a,b)

# LCM

def gcd(a,b): 
	if a == 0: 
		return b 
	return gcd(b % a, a) 

def lcm(a,b): 
	return (a / gcd(a,b))* b 
 
a = int(input("Enter value a: "))
b = int(input("Enter value b: "))
print('LCM of', a, 'and', b, 'is', lcm(a, b)) 

