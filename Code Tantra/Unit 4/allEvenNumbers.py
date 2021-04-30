# WAP to print all even numbers of a list using list comprehension

s = input("Enter elements separated by a comma :").split(",")
l = [int(i) for i in s if int(i) % 2 == 0]
print("Even numbers in the list: ", l)
