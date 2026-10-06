# OOP = Object-Oriented Programming

It is a way of writing programs by organizing code around objects.
In Python, we can represent this using a class and objects.
It includes Properties & Action

# A class is like a blueprint/template.
Syntax:
class Class_name:
    pass

Here pass means this class doesn't have anything and we can't make empty class that's why we are using term call pass.

##
Class = Blueprint
Object = Actual thing created from blueprint

# An object is an instance of a class.

class Class_name:
    pass

Classname = Class_name()

# Example:
class Car:
    pass
car1 = Car()

Car       → Class
car1      → Object
Car()     → Creates the object


# __init__()
__init__() is called automatically when you create an object.

# self refers to the current object.

self tells Python which object's data we are working with.

Syntax

class Class_name():
      def __init(self, Variable_1, Variable_2):
      self.Variable_1=Variable_1
      self.Variable_2=Variable_2

ClassName = Class_name(Value 1, Value 2)        --> Creating object
ClassName.Variable_1                           --> Calling object
print(ClassName.Variable_1)

# A method is basically a function inside a class.

# The Four Main OOP Concepts:
1. Encapsulation
Keeping data and methods together and controlling access to data.

2. Inheritance
One class can inherit properties and methods from another class.

3. Polymorphism
Same method name, different behavior.

4. Abstraction
Showing only the important details and hiding unnecessary implementation details.


OOP
│
├── 1. Class
│
├── 2. Object
│
├── 3. __init__()
│
├── 4. self
│
├── 5. Attributes / Properties
│
├── 6. Methods
│
├── 7. Instance Variables
│
├── 8. Class Variables
│
├── 9. Encapsulation
│
├── 10. Inheritance
│
├── 11. Method Overriding
│
├── 12. super()
│
├── 13. Polymorphism
│
├── 14. Abstraction
│
└── 15. OOP Project