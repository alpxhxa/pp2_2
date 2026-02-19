# ex 01
def add(a, b):
    return a + b

result = add(3, 4)
print(result)


# ex 02
def square(number):
    return number * number

print(square(5))


# ex 03
def is_even(num):
    return num % 2 == 0

print(is_even(10))


# ex 04
def get_full_name(first, last):
    return first + " " + last

name = get_full_name("Alice", "Smith")
print(name)


# ex 05
def max_number(a, b):
    if a > b:
        return a
    return b

print(max_number(8, 12))