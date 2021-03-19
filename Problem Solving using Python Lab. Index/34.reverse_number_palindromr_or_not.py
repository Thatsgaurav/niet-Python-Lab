# WAP to reverse the given number. Also check whether the given number is in palindrome or not. 

n = int(input("Enter number :"))
temp = n
rev = 0
 
while(n > 0):
    a = n % 10
    rev = rev * 10 + a
    n = n // 10
 
print("Reverse of given number", rev)
if(temp==rev):
    print("The number is a palindrome!")
else:
    print("The number isn't a palindrome!")  
      