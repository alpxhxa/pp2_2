#ex 01
def simple_gen():
    yield "A"
    yield "B"

g1 = simple_gen()
print(next(g1))
print(next(g1))

#ex 02
def step_gen():
    x = 10
    yield x
    x += 10
    yield x

g2 = step_gen()
print(next(g2))
print(next(g2))

#ex 03
def list_gen():
    yield [1, 2]
    yield [3, 4]

g3 = list_gen()
print(next(g3))
print(next(g3))

#ex 04
def mixed_gen():
    yield 1
    yield "Done"

g4 = mixed_gen()
print(next(g4))
print(next(g4))

#ex 05
def hello_gen():
    yield "Hello"
    yield "World"

g5 = hello_gen()
for word in g5:
    print(word)