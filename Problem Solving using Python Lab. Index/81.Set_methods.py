# WAP to implement various Set methods (Any 10) 

print("1.add()	Adds an element to the set")
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)

print("2.clear()	Removes all the elements from the set")
fruits = {"apple", "banana", "cherry"}
fruits.clear()
print(fruits)

print("3.copy()	Returns a copy of the set")
fruits = {"apple", "banana", "cherry"}
x = fruits.copy()
print(x)

print("4.difference()	Returns a set containing the difference between two or more sets")
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.difference(y)
print(z)

print("5.difference_update()	Removes the items in this set that are also included in another, specified set")
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.difference_update(y)
print(x)

print("6.pop()	Removes an element from the set")
fruits = {"apple", "banana", "cherry"}
fruits.pop()
print(fruits)

print("7.remove()	Removes the specified element")
fruits = {"apple", "banana", "cherry"}
fruits.remove("banana")
print(fruits)

print("8.discard()	Remove the specified item")
fruits = {"apple", "banana", "cherry"}
fruits.discard("banana")
print(fruits)

print("9.symmetric_difference()	Returns a set with the symmetric differences of two sets")
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.symmetric_difference(y)
print(z)

print("10.update()	Update the set with the union of this set and others")
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.update(y)
print(x)