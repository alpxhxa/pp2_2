a = "xyz"
b = input()

s = 0

for i in range(0,len(b),3):
    if a in b:
        s = s + 1

print(s)
