# WAP to find min, max and average of elements of a list having numeric data

lst = []
n = int(input("How many numbers: "))
for i in range(0, n):
    ele = int(input("Enter number "))
    lst.append(ele)

maximum = max(lst)
print("Maximum element in the list is :", maximum, "")
minimum = min(lst)
print("Minimum element in the list is :", int(minimum))
sum = sum(lst)
length = len(lst)
average = sum/length
print("Average =", "", average)
