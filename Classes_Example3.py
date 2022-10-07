''' Python3 program to demonstrate working of a class'''

class Example3:

	# A simple class
	# attribute
	attr1 = "Human"
	attr2 = "Ayushi"

	# A sample method
	def intro(self):
		print("I'm ", self.attr1)
		print("Hi, I'm ", self.attr2)

Sentence = Example3()

# Accessing class attributes and method through objects
print(Sentence.attr1)
Sentence.intro()
