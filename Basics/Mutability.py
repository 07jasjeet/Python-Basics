hashNum = 1
def addSpace():
    global hashNum
    print(f"\n\n#{hashNum}")
    hashNum += 1

def printIds():
    print(f'a = {id(a)}')
    print(f'b = {id(b)}')

addSpace()
'''
#1
When we create a new variable and assign it to something,
the variable has the same address as that of the assigned.
'''
a = [55]
b = a
# Here, a and b have the same address, we can confirm this
# by using the `id()` function.
printIds()

# So ofcourse they also share the same value as the list
# address is the same.

addSpace()
'''
#2
Creating two lists (even if they are the same), they will have
different adsresses
'''

a = []
b = []

printIds()

addSpace()
'''
#3
Python has this optimisation where, if we assign same values to
two different variables, both of those variables will access the
same location where the variable is stored.

If we change one variable, it won't modify the address's value,
but change the address by creating the new value in new address.
'''

a = 85
b = 85

printIds()

addSpace()
'''
#4
Assignment symbol (=) basically means assigning address to a name.
Immutable types:
    tuples
    int
    float
    booleans
    strings
    and more.

When we try to assign new values to variable that links to any of
these type's addresses, python creates a new variable at a new address.
'''

a = "Hello "
b = a

printIds()

a += "World"

printIds()

addSpace()
'''
#5
Mutable parameters are a bad idea.

When a class is created, all functions are evaluated and default addresses are given
to default values of the parameters. This means, when we edit the value on one location,
all the class objects (having the same location) will observe the effect
'''

# Code that has mutable paramters
"""
class Student:
    '''
    `grades: list[int] = []` is our fault part in this class as it is mutable. 
    '''
    def __init__(self, name: str, grades: list[int] = []) -> None:
        self.name = name
        self.grades = grades

    def take_exam(self, result: int):
        self.grades.append(result)

a = Student('a')
b = Student('b')
a.take_exam(90)

print(a.grades)
print(b.grades)     # We didn't assign any grades to b, why does he have 90 in his list?
"""

# Fixed code
from typing import Optional

class Student:
    '''
    We should set the default value to None. This sould work.
    What we can also do is apply optional type which lets python know
    that the argument is optional.
    '''
    def __init__(self, name: str, grades: Optional[list[int]] = None) -> None:
        self.name = name
        self.grades = grades or []      # This means, if None is found, grades is assigned a new empty list.

    def take_exam(self, result: int):
        self.grades.append(result)

a = Student('a')
b = Student('b')
a.take_exam(90)

print(a.grades)
print(b.grades)