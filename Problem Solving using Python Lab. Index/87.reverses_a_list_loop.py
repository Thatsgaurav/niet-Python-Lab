# WAP that reverses a list using loop

NumList = []

Number = int(input("Please enter the Total Number of List Elements: "))
for i in range(1, Number + 1):
    value = int(input("Please enter the Value of %d Element : " %i))
    NumList.append(value)

j = Number - 1
i = 0

while(i < j):
    temp = NumList[i]
    NumList[i] = NumList[j]
    NumList[j] = temp
    i = i + 1
    j = j - 1
    
print("\nThe Result of a Reverse List =  ", NumList)