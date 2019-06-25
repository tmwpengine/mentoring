def print_message(message):
    # this is the enclosing function
    def print_message_inside():
        # The nested function
        print(message)

    print_message_inside()

print_message("Hi there")


def print_message_with_non_local(msg):
    print(msg)

    def print_again():
        # Here we are using the nonlocal keyword
        nonlocal msg
        msg = "Text has changed !!"
        print(msg)

    print_again()

    print(msg)

print_message_with_non_local("original text")


# example closure
def store_message(message):

    def data_transmitter():
        print(message)

    return data_transmitter

f = store_message("Away we go!")

# f()

del store_message


f()


# another example closure
def make_multiplier_of(n):
    def multiplier(x):
        return x * n
    return multiplier

multiplied_by_five = make_multiplier_of(5)
multiplied_by_fifty = make_multiplier_of(50)

del make_multiplier_of

print(multiplied_by_five(10))
print(multiplied_by_fifty(10))

print(dir(multiplied_by_five))


def do_something():
    print("something")

f5 = do_something
print(f5.__closure__)

print(multiplied_by_five.__closure__)
print(type(multiplied_by_five.__closure__))
print(len(multiplied_by_five.__closure__))
print(dir(multiplied_by_five.__closure__[0]))
print(multiplied_by_five.__closure__[0].cell_contents)
