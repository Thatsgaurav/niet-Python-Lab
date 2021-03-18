# . WAP to compute the sum of following series up to the nth term.1 + 𝑥ଵ/1! + 𝑥ଶ/2! +𝑥 ଷ/3! + ……. 

n=int(input("Enter the number of terms:"))
x=int(input("Enter the value of x:"))
sum1=1
for i in range(2,n+1):
    sum1=sum1+((x**i)/i)
print("The sum of series is",round(sum1,2))