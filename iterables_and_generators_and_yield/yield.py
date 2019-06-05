# Generator function
def simple_generator_function():
    print("Hi")
    yield
    print("how")
    yield
    print("are")
    yield
    print("you")
    yield
    print("today")
    yield


my_generator = simple_generator_function()
print("Starting generator")
next(my_generator)  # Hi
next(my_generator)  # how
next(my_generator)  # are
next(my_generator)  # you
next(my_generator)  # today


def countdown(num):
    print("Count Down!")
    while num > 0:
        print(num)
        yield num
        num -= 1

my_generator = countdown(5)

print(my_generator)

next(my_generator)  # first time we call next will execute through the function till we hit yield
next(my_generator)  # second time will continue from the yield, decrement num and continue execution till we hit yield
next(my_generator)  # and so on
next(my_generator)  # and so on
next(my_generator)  # and so on
# Uncommenting the next line will cause a StopIteration exception because there's no more values to iterate
# next(my_generator)




