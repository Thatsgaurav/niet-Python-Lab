# Write a Python function to reverse a string
# Using recursion

def reverse(str):
    new_str = ''
    i = len(str)-1
    while i>=0:
        new_str += str[i]
        i -= 1
    return new_str
str = input("Enter a string : ")
print("The reversed string is : ", reverse(str))


# def reverse(s):
#     if len(s) == 0:
#         return s
#     else:
#         return reverse(s[1:]) + s[0]
#
# s = input("Enter String: ")
#
# print("The original string  is : ", end="")
# print(s)
#
# print("The reversed string is : ", end="")
# print(reverse(s))


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
