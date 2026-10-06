class Car:

    def __init__(self, brand, color):
        self.brand = brand
        self.color = color
car1 = Car("BMW", "Black")
print(car1.brand)


class Animal:

    def eat(self):
        print("Animal is eating")


class Dog(Animal):

    def bark(self):
        print("Dog is barking")

dog =Dog()
dog.eat()
dog.bark()

class Dog:

    def sound(self):
        print("Bark")


class Cat:

    def sound(self):
        print("Meow")


class Student:
    def __init__(self, name , age , course):
        self.name = name
        self.age= age
        self.course = course

student_1 = Student("Amit",24,"Python")
student_2 = Student("Rakesh", 34, "ML/AL")

print(student_1.name)
print(student_1.age)
print(student_1.course)

print(student_2.name)
print(student_2.age)
print(student_2.course)


        