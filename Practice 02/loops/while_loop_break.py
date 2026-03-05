#ex 01
i = 1
while True:
    print(i)
    if i == 5:
        break
    i += 1

#ex 02
num = 0
while num < 10:
    if num == 4:
        break
    print(num)
    num += 1

#ex 03
password = "1234"
attempt = ""
while True:
    attempt = "1234"
    if attempt == password:
        print("Access granted")
        break

#ex 04
i = 0
while True:
    print("Running")
    i += 1
    if i == 3:
        break

#ex 05
numbers = [1, 3, 5, 7]
i = 0
while i < len(numbers):
    if numbers[i] == 5:
        break
    print(numbers[i])
    i += 1