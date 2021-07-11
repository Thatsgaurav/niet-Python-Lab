# 1.	Write a program illustrating class definition and accessing class members.

# class definition
class Dog:
	
	attr1 = "mammal"
	attr2 = "dog"

	def fun(self):
		print("I'm a", self.attr1) #class members
		print("I'm a", self.attr2) #class members

Rodger = Dog()
print(Rodger.attr1)
Rodger.fun()
