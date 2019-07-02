test_dict = {'a': 'b'}
test_string = 'Foobar'
test_int = 1


# This is bad, too broad an exception
try:
    print(test_dict['c'])
except:
    pass


try:
    print(test_dict['c'])
except KeyError:
    print("KeyError")
except Exception as e:
    print(e.args)

try:
    print(test_string + test_int)
except TypeError:
    print("Cannot concatenate string and int objects")
except KeyError:
    print('KeyError')
finally:
    print("In finally")

print("In next line")


if test_dict.get('c'):
    value_of_c = test_dict['c']

try:
    value_of_c = test_dict['c']
except KeyError:
    value_of_c = "c not found"

print(value_of_c)
