"""
Generators are objects that you can itrerate over only once.
They don't store values in memory, they generate them on the fly.
"""
import sys


new_list = [x for x in range(0, 10)]

print("You can iterate over a list")
for i in new_list:
    print(i)

print("again and again")
for i in new_list:
    print(i)

new_generator = (x for x in range(0, 10))
print(type(new_generator))

print("You can iterate over a generator once")
for i in new_generator:
    print(i)

print("But not a second time")
for i in new_generator:
    print(i)


my_generator = (i*5 for i in range(100) if i % 3 == 0 or i % 5 == 0)
my_list = [i*5 for i in range(100) if i % 3 == 0 or i % 5 == 0]

print(f'Generator size : {sys.getsizeof(my_generator)}')
print(f'List size: {sys.getsizeof(my_list)}')