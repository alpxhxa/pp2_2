#ex 01
def my_range(n):
    i = 0
    while i < n:
        yield i
        i += 1

for val in my_range(3):
    print(val)

#ex 02
def fib(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

print(list(fib(3)))

#ex 03
def even_nums(limit):
    for i in range(limit):
        if i % 2 == 0:
            yield i

for n in even_nums(5):
    print(n)

#ex 04
def powers(n):
    for i in range(n):
        yield 2**i

print(list(powers(3)))

#ex 05
def reverse_str(s):
    for i in range(len(s) - 1, -1, -1):
        yield s[i]

for char in reverse_str("Py"):
    print(char)#ex 01
def my_range(n):
    i = 0
    while i < n:
        yield i
        i += 1

for val in my_range(3):
    print(val)

#ex 02
def fib(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

print(list(fib(3)))

#ex 03
def even_nums(limit):
    for i in range(limit):
        if i % 2 == 0:
            yield i

for n in even_nums(5):
    print(n)

#ex 04
def powers(n):
    for i in range(n):
        yield 2**i

print(list(powers(3)))

#ex 05
def reverse_str(s):
    for i in range(len(s) - 1, -1, -1):
        yield s[i]

for char in reverse_str("Py"):
    print(char)