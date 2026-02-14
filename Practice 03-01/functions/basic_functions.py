# ex 01
def greet():
    print("Hello, world!")

greet()


# ex 02
def show_age():
    age = 18
    print("I am", age)

show_age()


# ex 03
def say_hi():
    print("Hi!")

def start():
    say_hi()

start()


# ex 04
def check_number():
    num = -5
    if num > 0:
        print("Positive")
    else:
        print("Negative")

check_number()


# ex 05
def outer():
    def inner():
        print("Inside inner function")
    inner()

outer()