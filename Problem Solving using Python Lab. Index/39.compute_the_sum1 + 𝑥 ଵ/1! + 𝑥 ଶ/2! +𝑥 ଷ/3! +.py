# WAP to compute the sum of following series up to the nth term. 1 + 𝑥 ଵ/1! + 𝑥 ଶ/2! +𝑥 ଷ/3! + ……. 

n=int(input("Enter the number of terms:"))
x=int(input("Enter the value of x:"))
sum1=1
for i in range(1,n):
    fact = 1
    for j in range(1,i+1):
        fact *= j
        sum += (x**i/fact)
        print("The sum of series is", sum)