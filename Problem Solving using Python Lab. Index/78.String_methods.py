# WAP to implement various String methods (Any 10)

print("1.capitalize()")
txt = "hello, and welcome to my world."
x = txt.capitalize()
print (x)

print("2.casefold()")
txt = "Hello, And Welcome To My World!"
x = txt.casefold()
print(x)

print("3.center()")
txt = "banana"
x = txt.center(20)
print(x)

print("4.count()")
txt = "I love apples, apple are my favorite fruit"
x = txt.count("apple")
print(x)

print("5.find()")
txt = "Hello, welcome to my world."
x = txt.find("welcome")
print(x)

print("6.format()")
txt = "For only {price:.2f} dollars!"
print(txt.format(price = 49))

print("7.index()")
txt = "Hello, welcome to my world."
x = txt.index("welcome")
print(x)

print("8.replace()")
txt = "I like bananas"
x = txt.replace("bananas", "apples")
print(x)

print("9.split()")
txt = "welcome to the jungle"
x = txt.split()
print(x)

print("10.translate()")
mydict = {83:  80}
txt = "Hello Sam!"
print(txt.translate(mydict))