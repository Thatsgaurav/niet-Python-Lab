# WAP that prompts user to enter an alphabet and then print all the words that starts with that alphabet. 

str1 = input("Enter any sentance :")
alpha = input("Enter the alphabet :")
print("Word starts with",alpha,"are :")
for i in str1.split(alpha):
    print(i,end=",")