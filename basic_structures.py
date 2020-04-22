# String (Immutable)
s = 'some string'

multi_line_string = a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""

first_name = 'Tony'
last_name = 'milan'
full_name = f'Full name is {first_name} {last_name}'  # interpolation Python3
full_name2 = 'Full name is {first_name} {last_name}'.format(first_name=first_name, last_name=last_name)  # Python2

print(full_name[1])
print(full_name[1:5])
print(len(full_name))
print(full_name.strip())
print(full_name.lower())
print(full_name.replace('Tony', 'Jose'))
print(full_name.split())
print('Tony' in full_name)


# List (Mutable)
list_of_ints = [1, 1, 2, 2]
list_of_strings = ['a', 'b', 'c']
mixed_list = [1, True, 'a', [5, 6, 7]]

print(list_of_ints[2])

for item in list_of_ints:
    print(item)

list_of_ints[1] = 100
print(list_of_ints)

if 'a' in list_of_strings:
    print(True)

print(len(list_of_ints))

list_of_ints.append(666)
list_of_strings.remove('a')

merged_list = list_of_ints + list_of_strings
copied_list = list_of_strings.copy()

# Tuple (Immutable): manipulate data the same way you would a list

tuple_ints = (1, 2, 3, 4)

# Set (Mutable)
some_set = {'a', 'a', 'b', 'b'}
print(some_set)  # Note they cannot contain duplicates
some_set.add('c')
some_set.update('d', 'e', 'f')
print(some_set)

new_set = {'g', 'h'}

merged_set = some_set.union(new_set)

# Dictionaries (Mutable)
d = {'first_name': 'Tony', 'last_name': 'Milan'}
first_name = d['first_name']
last_name = d['last_name']
print(f'{first_name} {last_name}')

d['address'] = 'Clare'
print(d)
d['address'] = 'Clarecastle'
print(d)

d.pop('address')
print(d)

for key, value in d.items():
    print(key, value)

d_keys = d.keys()
print(d_keys)
d_values = d.values()
print(d_values)

if 'first_name' in d:
    print(d['first_name'])

try:
    middle_name = d['middle_name']
except KeyError:
    middle_name = d.get('middle_name')
    print(type(middle_name))
    if middle_name is None:
        print('middle name is not in dict')

nested_dict = {
    'person': {
        'name': 'Tony',
        'address': 'Clare'
    }
}

print(nested_dict['person']['name'])

# Mutable vs Immutable
s = 'Tony'
print(id(s))
s += 'Milan'
print(id(s))

s1 = 'first string'
print(id(s1))

l = [1, 2]
print(id(l))
l.append(3)
print(id(l))
