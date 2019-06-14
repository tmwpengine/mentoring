def demo_a_list_is_mutable(l):
    print(f'First index of list is {l[0]}')

    l[0] = 'changed'

    print(f'First index of list is now {l[0]}')

    print(f'ID of list is {id(l)} when value is {l}')

    l += [5, 6, 7, 8]

    print(f'ID of list remains {id(l)} when value is changed to{l}')

    l2 = l

    print(f'ID of l is {id(l)} and the ID of l2 is {id(l2)}')

    l.append(100)

    print(f'ID of l is {id(l)} and the ID of l2 is {id(l2)}')
    print(f'Value of l is {l} and the value of l2 is {l2}')

    l2.append(200)

    print(f'ID of l is {id(l)} and the ID of l2 is {id(l2)}')
    print(f'Value of l is {l} and the value of l2 is {l2}')


def demo_a_tuple_is_immutable(t):
    print(f'First index of tuple is {t[0]}')

    try:
        t[0] = 'changed'
    except TypeError as e:
        print("You're seeing this because we tried to change a value in a tuple!!")
        print(f'It shit the bed with exception {e.args[0]}')

    print(f'ID of tuple is {id(t)} when value is {t}')

    t += (5, 6, 7, 8)

    print(f'ID of tuple changes to {id(t)} when value is changed to {t}')


def demo_an_int_is_immutable(i):
    print(f'ID of int is {id(i)} when value is {i}')
    i += 1
    print(f'ID of int is now {id(i)} when value is changed to {i}')


def demo_mutable_object_in_immutable_container():
    l = ['a', 'b', 'c']
    t = ('d', l)

    print(f'ID of t at this point is {id(t)}')
    print(f'Value of t at this point is {t}')

    l[2] = 'ZZZ'

    print(f'ID of t at this point is {id(t)}')
    print(f'Value of t at this point is {t}')


demo_a_list_is_mutable([1, 2, 3, 4])
demo_a_tuple_is_immutable((1, 2, 3, 4))
demo_an_int_is_immutable(1)
demo_mutable_object_in_immutable_container()


# Demo pass by reference
def update_list(l):
    l += [10]


l = [5, 6]
print(id(l))

update_list(l)

print(l)
print(id(l))


# Demo pass by value
def updateNumber(n):
    print(id(n))
    n += 10

n = 5
print(id(n))
updateNumber(n)
print(n)
