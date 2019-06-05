"""
These iterables are handy because you can read them as much as you wish,
but you store all the values in memory and it’s not always what you want when you have a lot of values.
"""

# Basic
def print_numbers_between_one_and_ten():
    for num in range(0, 11):
        print(num)


print_numbers_between_one_and_ten()


def print_numbers_in_a_list_divisible_by_two(l):
    for num in l:
        if num % 2 == 0:
            print(num)

print_numbers_in_a_list_divisible_by_two([x for x in range(11)])


def reverse_a_dict(d):
    new_d = {}
    for key, value in d.items():
        new_d[value] = key

    return new_d

print(reverse_a_dict({"a": 1, "b": 2}))


def print_letters_in_string(s):
    for char in s:
        print(char)

print_letters_in_string("hello")


# Comprehensions

def remove_none_types_from_list(l):
    copy_l = l
    new_l = []

    # The basic way
    for obj in l:
        if obj is not None:
            new_l.append(obj)

    print(new_l)

    # Using a comprehension
    print([obj for obj in copy_l if obj is not None])


remove_none_types_from_list(['a', 1, {'a': 1}, range(0, 3), None])


def reverse_a_dict_using_a_comprehension(d):
    return {value: key for key, value in d.items()}

print(reverse_a_dict_using_a_comprehension({'a': 1, 'b': 2}))