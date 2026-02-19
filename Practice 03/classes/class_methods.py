# ex 01
class Person:
    def greet(self):
        print("Hello!")

p = Person()
p.greet()


# ex 02
class Math:
    def square(self, x):
        return x * x

m = Math()
print(m.square(6))


# ex 03
class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

account = BankAccount(100)
print(account.deposit(50))


# ex 04
class Counter:
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1

c = Counter()
c.increment()
print(c.count)


# ex 05
class Rectangle:
    def area(self, width, height):
        return width * height

r = Rectangle()
print(r.area(4, 5))