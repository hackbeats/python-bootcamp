#Call declaration program

''' Python3 program to show that the variables with a value assigned in the class declaration, are class variables and variables inside methods and constructors are instance
variables.'''



class Example4:

	# Class Variable
	name = 'Human'
   

	# The init method or constructor
	def __init__(self,age, color):

		# Instance Variable
		self.age = age
		self.color = color
       


# Objects of class
Sentence = Example4(20, "brown")
Sentence2 = Example4(20, "brown")

print('Sentence details:')
print('She is: ', Sentence.name)
print('Age: ', Sentence.age)
print('Color: ', Sentence.color)

print('\nSentence 2 details:')
print('He is: ', Sentence2.name)
print('Age: ', Sentence2.age)
print('Color: ', Sentence2.color)

# Class variables can be accessed using class
# name also
print("\nAccessing class variable using class name")
print(Example4.name)
