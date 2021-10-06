#Creating a Class here
class SchoolMembers:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('The School meber is {} whose age is {} .' .format(self.name, self.age))
    def introduce(self):
        print('Hello, My name is {} and my age is {} .'.format(self.name, self.age))

#Creating an instance of the class, i.e, object of class SchoolMembers..
p = SchoolMembers('Munish',21)

#Calling the method introduce of 'p' object which belongs to class SchoolMembers
p.introduce()

#The output will be:
# The School meber is Munish whose age is 21 .
# Hello, My name is Munish and my age is 21 .
