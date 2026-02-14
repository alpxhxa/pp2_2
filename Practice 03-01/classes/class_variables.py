# ex 01
class Person:
    species = "Human"

p1 = Person()
print(p1.species)


# ex 02
class Dog:
    legs = 4

d = Dog()
print(d.legs)


# ex 03
class Student:
    school = "High School"

    def __init__(self, name):
        self.name = name

s1 = Student("Alex")
s2 = Student("Sam")
print(s1.school, s2.school)


# ex 04
class Counter:
    count = 0

    def __init__(self):
        Counter.count += 1

c1 = Counter()
c2 = Counter()
print(Counter.count)


# ex 05
class Product:
    tax = 0.2

    def __init__(self, price):
        self.price = price

    def price_with_tax(self):
        return self.price * (1 + Product.tax)

item = Product(100)
print(item.price_with_tax())