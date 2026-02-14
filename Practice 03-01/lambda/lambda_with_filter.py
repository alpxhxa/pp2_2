# ex 01
numbers = [1, 2, 3, 4, 5]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)


# ex 02
numbers = [10, 25, 30, 5, 40]
greater_than_20 = list(filter(lambda x: x > 20, numbers))
print(greater_than_20)


# ex 03
names = ["Alex", "John", "Sam", "Alina"]
starts_with_a = list(filter(lambda name: name.startswith("A"), names))
print(starts_with_a)


# ex 04
words = ["hi", "hello", "a", "world"]
long_words = list(filter(lambda word: len(word) > 3, words))
print(long_words)


# ex 05
numbers = [-5, 3, -2, 8, 0]
positives = list(filter(lambda x: x > 0, numbers))
print(positives)