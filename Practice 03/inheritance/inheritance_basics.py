# ex 01
class Animal:
    def speak(self):
        print("Animal makes a sound")

class Dog(Animal):
    pass

d = Dog()
d.speak()


# ex 02
class Person:
    def greet(self):
        print("Hello!")

class Student(Person):
    def study(self):
        print("Studying...")

s = Student()
s.greet()
s.study()


# ex 03
class Vehicle:
    def move(self):
        print("Moving")

class Car(Vehicle):
    def drive(self):
        print("Driving")

c = Car()
c.move()
c.drive()


# ex 04
class Shape:
    def info(self):
        print("This is a shape")

class Circle(Shape):
    pass

circle = Circle()
circle.info()


# ex 05
class Employee:
    def work(self):
        print("Working...")

class Manager(Employee):
    def manage(self):
        print("Managing...")

m = Manager()
m.work()
m.manage()