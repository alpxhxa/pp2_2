# ex 01
numbers = [1, 2, 3, 4]
squares = list(map(lambda x: x * x, numbers))
print(squares)


# ex 02
numbers = [1, 2, 3, 4]
doubled = list(map(lambda x: x * 2, numbers))
print(doubled)


# ex 03
names = ["alex", "john", "sam"]
capitalized = list(map(lambda name: name.capitalize(), names))
print(capitalized)


# ex 04
temps_c = [0, 10, 20, 30]
temps_f = list(map(lambda c: c * 9/5 + 32, temps_c))
print(temps_f)


# ex 05
numbers = [1, 2, 3]
strings = list(map(lambda x: "Number: " + str(x), numbers))
print(strings)