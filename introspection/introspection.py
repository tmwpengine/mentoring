s = "HiWillIAm".upper()

print(len(s))
print(type(s))

if type(s) is str:
    print("Booo Ya")

if isinstance(s, str):
    print("Boo ya")

print(dir(s))
print(s.isalpha())

l = [0, 1, 2, 3, 'william', 'zilliam', 'aaaa']

print(dir(l))
print(l.count('william'))

