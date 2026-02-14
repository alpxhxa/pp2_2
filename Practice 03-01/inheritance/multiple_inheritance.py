# ex 01
class A:
    def method_a(self):
        print("Method A")

class B:
    def method_b(self):
        print("Method B")

class C(A, B):
    pass

c = C()
c.method_a()
c.method_b()


# ex 02
class Fly:
    def fly(self):
        print("Flying")

class Swim:
    def swim(self):
        print("Swimming")

class Duck(Fly, Swim):
    pass

d = Duck()
d.fly()
d.swim()


# ex 03
class Father:
    def skill(self):
        print("Carpentry")

class Mother:
    def talent(self):
        print("Painting")

class Child(Father, Mother):
    pass

child = Child()
child.skill()
child.talent()


# ex 04
class X:
    def greet(self):
        print("Hello from X")

class Y:
    def greet(self):
        print("Hello from Y")

class Z(X, Y):
    pass

z = Z()
z.greet()   # вызовется метод из X (MRO)


# ex 05
class Writer:
    def write(self):
        print("Writing...")

class Speaker:
    def speak(self):
        print("Speaking...")

class Author(Writer, Speaker):
    pass

a = Author()
a.write()
a.speak()