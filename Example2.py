'''Greetings to the person'''

class Example2:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def me(self):
    print("Hello my name is " + self.name)

e2 = Example2 ("Ayushi", 20)
e2.me()


'''to delete object properties'''
del e2.age

'''to delete whole object'''
del e2