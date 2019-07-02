from functools import partial


def multiply(x, y):
    return x * y


def double(x):
    return multiply(x, 2)


def triple(x):
    return multiply(x, 3)

print(multiply(2, 1))
print(double(4))
print(triple(4))


# Using partial functions
double = partial(multiply, y=2)
triple = partial(multiply, y=3)

print(double(4))
print(triple(4))

# partial functions store info about the original functions that spawned them
print(double.func)
print(double.keywords)

for i in range(1, 11):
    f = partial(multiply, i)
    print(f(10))
