#ex 01
gen1 = (x**2 for x in range(3))
for n in gen1:
    print(n)

#ex 02
gen2 = (s.upper() for s in ["a", "b"])
print(next(gen2))
print(next(gen2))

#ex 03
gen3 = (x for x in range(10) if x % 3 == 0)
print(list(gen3))

#ex 04
nums = [10, 20, 30]
gen4 = (n + 1 for n in nums)
for res in gen4:
    print(res)

#ex 05
gen5 = (f"ID:{i}" for i in range(2))
print(next(gen5))
print(next(gen5))