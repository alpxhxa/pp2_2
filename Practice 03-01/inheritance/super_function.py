# ex 01
class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

d = Dog("Buddy", "Labrador")
print(d.name, d.breed)


# ex 02
class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self, name, grade):
        super().__init__(name)
        self.grade = grade

s = Student("Alex", 95)
print(s.name, s.grade)


# ex 03
class Vehicle:
    def __init__(self):
        print("Vehicle created")

class Car(Vehicle):
    def __init__(self):
        super().__init__()
        print("Car created")

c = Car()


# ex 04
class A:
    def greet(self):
        print("Hello from A")

class B(A):
    def greet(self):
        super().greet()
        print("Hello from B")

b = B()
b.greet()


# ex 05
class Employee:
    def __init__(self, salary):
        self.salary = salary

class Manager(Employee):
    def __init__(self, salary, bonus):
        super().__init__(salary)
        self.bonus = bonus

m = Manager(5000, 1000)
print(m.salary, m.bonus)