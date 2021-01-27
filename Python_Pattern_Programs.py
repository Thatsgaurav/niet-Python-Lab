# Pyramid Pattern Program

# def pattern(n):
#     k = 2 * n - 2
#     for i in range(0,n):
#            for j in range(0,k):
#                print(end=" ")
#            k = k - 1
#            for j in range(0, i+1):
#                 print("*", end=" ")
#            print()
# pattern(5)

r = 6
for i in range(1, r + 1):
    for j in range(1, i - 1):
        print(j, end=" ")
    for j in range(i - 1, 0, -1):
        print(j, end=" ")
    print()
