# Write a Python function to reverse a string
# Using recursion

def reverse(s):
    if len(s) == 0:
        return s
    else:
        return reverse(s[1:]) + s[0]

s = input("Enter String: ")

print("The original string  is : ", end="")
print(s)

print("The reversed string is : ", end="")
print(reverse(s))


# Using Loop
# def reverse(s):
#     str = ""
#     for i in s:
#         str = i + str
#     return str
#
# s = input("Enter String: ")
#
# print("The original string  is : ", end="")
# print(s)
#
# print("The reversed string is : ", end="")
# print(reverse(s))
