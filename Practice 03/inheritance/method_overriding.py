# ex 01
class Animal:
    def speak(self):
        print("Animal sound")

class Dog(Animal):
    def speak(self):
        print("Woof!")

d = Dog()
d.speak()


# ex 02
class Person:
    def role(self):
        print("Person")

class Student(Person):
    def role(self):
        print("Student")

s = Student()
s.role()


# ex 03
class Shape:
    def area(self):
        print("Calculating area")

class Rectangle(Shape):
    def area(self):
        print("Rectangle area = width * height")

r = Rectangle()
r.area()


# ex 04
class Vehicle:
    def move(self):
        print("Vehicle moving")

class Bike(Vehicle):
    def move(self):
        print("Bike riding")

b = Bike()
b.move()


# ex 05
class Employee:
    def work(self):
        print("Employee working")

class Developer(Employee):
    def work(self):
        print("Developer coding")

dev = Developer()
dev.work()