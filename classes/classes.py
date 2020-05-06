# A Class is like an object constructor, or a "blueprint" for creating objects.
class SimpleClass:
    """A class in it's most basic form, note the CamelCase format used in naming"""
    class_var = 5  # This is a class variables, it's shared between all instances of the class


# Instantiate an instance of the above class, creating an object of type SimpleClass
my_class1 = SimpleClass()
print(my_class1.class_var)

my_class2 = SimpleClass()
print(my_class2.class_var)

# Note that updating the class variable `class_var` affects the current instances (my_class1, my_class2)
# and all future instances of the class
SimpleClass.class_var = 100
print(my_class1.class_var, my_class2.class_var)


# Use the _class_init__() function to assign values to object properties
class Person:
    """The __init__() function is called automatically every time the class is being used to create a new object"""
    def __init__(self, name, age):
        """
        Variables declared inside the __init__ are instance variables.
        These are tied to the particular object instance of the class, hence the contents of an instance variable
        are completely independent from one object instance to the other
        """
        self.name = name
        self.age = age


person = Person("Tony", 21)

print(person.name)
print(person.age)


# Create your own functions encapsulated within the class
class Person:
    """
    The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.
    It does not have to be named self , you can call it whatever you like, but it has to be the first parameter of any function in the class:
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def is_teen(self):
        if self.age < 19:
            return True
        return False

    def is_old_as_fuck(self):
        if self.age > 60:
            return True
        return False


person = Person('Tony', 'Milan', 21)
print(person.full_name())
print(person.is_teen())
print(person.is_old_as_fuck())
