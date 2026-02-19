#ex 01
nums = [1, 2, 3]
for n in iter(nums):
    print(n)

#ex 02
colors = ("red", "green", "blue")
it2 = iter(colors)
for color in it2:
    print(color)

#ex 03
it3 = iter("ABC")
for char in it3:
    print(char)

#ex 04
data = {'x': 100, 'y': 200}
it4 = iter(data.values())
for val in it4:
    print(val)

#ex 05
it5 = iter(range(2))
for i in it5:
    print(i)