def demo_use_of_args(first_arg, *args):
    print(f'first_arg is {first_arg}')
    print(f'*args is {args} ')
    for arg in args:
        print(arg)

demo_use_of_args('required arg', 'non_required_arg1', 'non_required_arg2')
print('*********')
demo_use_of_args('required arg', *['non_required_arg1', 'non_required_arg2'])
print('*********')
demo_use_of_args('required arg', *[x for x in range(10)])
print('*********')
demo_use_of_args('required arg')
print('*********')


def demo_use_of_kwargs(first_arg, **kwargs):
    print(f'first_arg is {first_arg}')
    print(f'*args is {kwargs} ')
    for key, value in kwargs.items():
        print(f'key is {key} and value is {value}')


demo_use_of_kwargs('first_arg', name='Tony')
print('*********')

d= {'name': 'Tony'}

demo_use_of_kwargs('first_arg', **d)
print('*********')


def demo_use_of_default_arg(first_arg, second_arg=None):
    print(f'first_arg is {first_arg}')
    print(f'second arg is {second_arg}')
    if second_arg:
        print(f'second_arg is {second_arg}')


demo_use_of_default_arg('first_arg')
print('*********')
demo_use_of_default_arg('first_arg', 'second_arg')


def demo_bad_use_of_default_arg(second_arg=[]):
    """This is a bad thing, notice the way the value is persisted in the list every time the function is called.
    Don't default with mutable objects!!
    """
    print(f'second_arg is {second_arg}')
    second_arg.append('a')
    print(f'second_arg is {second_arg}')


demo_bad_use_of_default_arg()
print("when we run it the second time, look what happens")
demo_bad_use_of_default_arg()
