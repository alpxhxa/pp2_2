#ex 01
for i in range(5):
    if i == 2:
        continue
    print(i)

#ex 02
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)

#ex 03
for char in "python":
    if char == "h":
        continue
    print(char)

#ex 04
for i in range(1, 6):
    if i == 3:
        continue
    print(i * 2)

#ex 05
numbers = [1, 2, 3, 4, 5]
for n in numbers:
    if n == 4:
        continue
    print(n)