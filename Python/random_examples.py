import random

random_integer = random.randint(1, 10)
print(random_integer)

random_float = random.random()
print(random_float)

random_float1 = random.random() * 5
print(random_float1)

fruits = ["Cherry", "Apple", "Banana", "Orange"]
print(random.choice(fruits))

print(fruits[1])

fruits[2] = "Pear"
print(fruits)
