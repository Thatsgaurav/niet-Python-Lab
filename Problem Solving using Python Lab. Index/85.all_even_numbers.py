# WAP to print all even numbers of a list using list comprehension

list1 = [11,23,45,23,64,22,11,24]
even_nos = [num for num in list1 if num % 2 == 0]
print("Even numbers : ", even_nos)