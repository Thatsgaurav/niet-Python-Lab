# WAP to implement various Dictionary methods (Any 10)

print("1.clear()	Removes all the elements from the dictionary")
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.clear()
print(car)


print("2.copy()	Returns a copy of the dictionary")
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = car.copy()
print(x)

print("3.fromkeys()	Returns a dictionary with the specified keys and value")
x = ('key1', 'key2', 'key3')
y = 0
thisdict = dict.fromkeys(x, y)
print(thisdict)

print("4.get()	Returns the value of the specified key")
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = car.get("model")
print(x)

print("5.items()	Returns a list containing a tuple for each key value pair")
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = car.items()
print(x)

print("6.keys()	Returns a list containing the dictionary's keys")
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = car.keys()
print(x)

print("7.pop()	Removes the element with the specified key")
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.pop("model")
print(car)

print("8.popitem()	Removes the last inserted key-value pair")
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.popitem()
print(car)

print("9.update()	Updates the dictionary with the specified key-value pairs")
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.update({"color": "White"})
print(car)

print("10.values()	Returns a list of all the values in the dictionary")
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = car.values()
print(x)
