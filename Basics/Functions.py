
# Variable arguments upto infinity.
# `args` here is treated as a tuple.
def printArgs(*args):
    print(args)

printArgs(1,2,3,4,5)

# Key-word argunments
def printKwargs(**kwargs):
    print(kwargs)

printKwargs(apple = 1, banana = 2, carrot = 3)

# We can also use both be the order should be same as parameter order.
def printBothArgs(*args, **kwargs):
    print(args)
    print(kwargs)

# map(func, *iterables) --> map object
# Make an iterator that computes the function using arguments from each of the iterables. 
# Stops when the shortest iterable is exhausted.
myList = [1,2,3,4,5]
def square(num):
    return num**2

print("\n")

for item in map(square,myList):
    print(item)

print("\n")

# Filter function
# We need an actual filter logic for the filter function.
def checkEven(num):
        return num%2 == 0     # Function must return true or false for every iterable item.
    

for item in filter(checkEven,myList):
    print(item)

# Lambda Expressions
# In filter function, we can also do
filter(lambda num: num**2, myList)

# Nested Scopes

var = "Global variable"

def fun():
    # global var
    # print(var)        # We CANNOT print global var without removing local var. Workaround: Use global keyword.
    var = "Enclosing function local variable"

    def innerFun():
        var = "Local variable"

fun()