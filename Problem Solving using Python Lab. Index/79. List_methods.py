# WAP to implement various List methods (All)

print("1.>>>append() Adds an element at the end of the list")
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
print(fruits)

print("2.>>>clear()	Removes all the elements from the list")
fruits = ["apple", "banana", "cherry"]
fruits.clear()
print(fruits)

print("3.>>>copy()	Returns a copy of the list")
fruits = ["apple", "banana", "cherry"]
x = fruits.copy()
print(x)

print("4.>>>count()	Returns the number of elements with the specified value")
fruits = ["apple", "banana", "cherry"]
x = fruits.count("cherry")
print(x)

print("5.>>>extend()	Add the elements of a list (or any iterable), to the end of the current list")
fruits = ['apple', 'banana', 'cherry']
cars = ['Ford', 'BMW', 'Volvo']
fruits.extend(cars)
print(fruits)

print("6.>>>index()	Returns the index of the first element with the specified value")
fruits = ['apple', 'banana', 'cherry']
x = fruits.index("cherry")
print(x)

print("7.>>>insert()	Adds an element at the specified position")
fruits = ['apple', 'banana', 'cherry']
fruits.insert(1, "orange")
print(fruits)

print("8.>>>pop()	Removes the element at the specified position")
fruits = ['apple', 'banana', 'cherry']
fruits.pop(1)
print(fruits)

print("9.>>>remove()	Removes the first item with the specified value")
fruits = ['apple', 'banana', 'cherry']
fruits.remove("banana")
print(fruits)

print("10.>>>reverse()	Reverses the order of the list")
fruits = ['apple', 'banana', 'cherry']
fruits.reverse()
print(fruits)

print("11.>>>sort()	Sorts the list")
cars = ['Ford', 'BMW', 'Volvo']
cars.sort()
print(cars)

