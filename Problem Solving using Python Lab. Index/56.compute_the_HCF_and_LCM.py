# WAP to compute the HCF and LCM of two numbers using user defined function

def calc_hcf(n1,n2):
  if n1 > n2:
    small = n2
  else:
    small = n1
  for i in range(1,small + 1):
    if((n1 % i == 0) and (n2 % i == 0)):
      result = i
  return result
num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))
print("THE HCF OF ",num1," AND ",num2," IS : ",calc_hcf(num1, num2))

# LCM 

def lcm(x, y):
   if x > y:
       z = x
   else:
       z = y

   while(True):
       if((z % x == 0) and (z % y == 0)):
           lcm = z
           break
       z += 1

   return lcm

num1 = int(input("Enter first number:"))
num2 = int(input("Enter second number: "))
print(lcm(num1, num2))