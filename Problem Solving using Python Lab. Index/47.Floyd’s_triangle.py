# WAP to display the Floyd’s triangle.
# 1
# 2 3
# 4 5 6
# 7 8 9 10
# 11 12 13 14 15

rows = int(input("Please Enter the total Number of Rows  : "))
number = 1

print("Floyd's Triangle") 
for i in range(1, rows + 1):
    for j in range(1, i + 1):        
        print(number, end = '  ')
        number = number + 1
    print()