# ex 01
class Person:
    def __init__(self, name):
        self.name = name

p = Person("Alex")
print(p.name)


# ex 02
class Car:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

c = Car("Toyota", 2022)
print(c.brand, c.year)


# ex 03
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

s = Student("Sam", 95)
print(s.name, s.grade)


# ex 04
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

circle = Circle(5)
print(circle.area())


# ex 05
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

book = Book("1984", "Orwell")
print(book.title, book.author)