# ex 01
numbers = [5, 2, 9, 1]
sorted_numbers = sorted(numbers, key=lambda x: x)
print(sorted_numbers)


# ex 02
numbers = [5, -2, 9, -1]
sorted_by_absolute = sorted(numbers, key=lambda x: abs(x))
print(sorted_by_absolute)


# ex 03
names = ["Alex", "john", "Sam", "alina"]
sorted_case_insensitive = sorted(names, key=lambda name: name.lower())
print(sorted_case_insensitive)


# ex 04
students = [
    ("Alex", 85),
    ("John", 92),
    ("Sam", 78)
]

sorted_by_score = sorted(students, key=lambda student: student[1])
print(sorted_by_score)


# ex 05
words = ["apple", "kiwi", "banana", "pear"]
sorted_by_length = sorted(words, key=lambda word: len(word))
print(sorted_by_length)