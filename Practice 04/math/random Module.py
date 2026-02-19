#ex 01
import random
print(random.random())

#ex 02
import random
print(random.randint(1, 10))

#ex 03
import random
items = ['apple', 'banana', 'cherry']
print(random.choice(items))

#ex 04
import random
deck = [1, 2, 3, 4, 5]
random.shuffle(deck)
print(deck)

#ex 05
import random
print(random.randrange(0, 100, 5))