'''All classes have a function called __init__(),
 which is always executed when the class is being initiated
 '''

class Example1:
  def __init__(self, name, age):
    self.name = name
    self.age = age

e1 = Example1("Ayushi", 20)

print(e1.name)
print(e1.age)