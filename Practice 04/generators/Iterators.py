#ex 01
simple_list = [1, 2, 3]
it1 = iter(simple_list)
print(next(it1))
print(next(it1))

#ex 02
text = "Hi"
it2 = iter(text)
print(next(it2))
print(next(it2))

#ex 03
my_set = {10, 20}
it3 = iter(my_set)
print(next(it3))
print(next(it3))

#ex 04
mapping = {'a': 1, 'b': 2}
it4 = iter(mapping)
print(next(it4))
print(next(it4))

#ex 05
it5 = iter([5.5])
print(next(it5))