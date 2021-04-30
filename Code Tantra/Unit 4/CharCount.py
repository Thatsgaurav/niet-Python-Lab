# Write a program to find how many times each character is repeated in a given string.

# Take string as input from the console using input() function. Write a program to find how many times each character is repeated in a given string. Print each character in the string in sorted order with number of times it is repeated as shown in the example.

# Sample Input and Output:
# Please enter sentence: Hello Python!
# ' '	1
# '!'	1
# 'H'	1
# 'P'	1
# 'e'	1
# 'h'	1
# 'l'	2
# 'n'	1
# 'o'	2
# 't'	1
# 'y'	1
# [' ', '!', 'H', 'P', 'e', 'h', 'l', 'n', 'o', 't', 'y']

s = input("Please enter sentence: ")
l = []
for char in s:
    if char not in l:
        l.append(char)
l.sort()
for element in l:
    print("'"+str(element)+"'", s.count(element), sep="\t")
print(l)
