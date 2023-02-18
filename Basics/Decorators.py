import functools

give_access = True
'''
Wrapper function or decorator allows us to wrap another function in order to extend the behavior 
of the wrapped function, without permanently modifying it. In Decorators, functions are taken as 
the argument into another function and then called inside the wrapper function.
'''

def function_to_be_passed():
    print("Passed function exectued.")

def decorator(func):
    
    def reciever_function():
        if give_access:
            return func()
        else:
            return lambda:print("No access given in function 1.")

    return reciever_function

myFun = decorator(function_to_be_passed)
myFun()






# @ syntax
'''
There is another problem, lets say that our another_function is directly
called, that means, it'll again be able to recieve any type of function.
To solve this, we use @ syntax.
We have already annotated the decorator function.
'''
give_access = True

def another_decorator(func):
    '''
    We use the `@functools.wraps(func)` here because when we decorate another_func,
    its name and all documentation is lost, instead it will show name and documentation of another reciever.
    '''
    @functools.wraps(func)
    def another_reciever(*args, **kwargs):
        '''
        Another reciever's documentation
        '''
        if give_access:
            return func(*args, **kwargs)
        else:
            return lambda:print("No access given in function 2.")

    return another_reciever

# Now, whenever we call another_func(), it will always go to another_decorator(),
# and pass itself as the parameter.
@another_decorator
def another_func():
    '''
    Another function's documentation.
    '''
    return lambda:print("Another function executed.")

# This statement doesn't work only if we use @ syntax.
myFunc = another_decorator(another_func) 
myFunc()

# Only this works.
myFunc = another_func()    
myFunc()

# Without unctools.wraps(): This prints out another_reciever which means name of another_func is lost.
# With unctools.wraps(): This prints out the name fine. (another_func)
print(another_func.__name__) 

# Same case here as above.
print(another_func.__doc__)







'''
Now what do we do if our another_func() takes in an argument and
looks like this: 
    some_other_function(parameter)

We simply add *args, **kwargs to another_reciever so we can have unlimited number
of arguments, and also making out decorator flexible.
This has already been done above in another_reciever()
'''
@another_decorator
def some_other_function(parameter):
    return lambda:print(f"Some other function's parameter: {parameter}")

myFunc = some_other_function(55)
myFunc()







'''
Decorators with parameters.
Lets take an example of a security login.
'''
print('\n\n\tSecurity function\n')

user = {"username": "jasjeet", "access-level": "guest"}

def make_secure(access_level):
    '''
    This outer function helps take in arguments
    for the @ function.
    '''
    def decorator(func):

        @functools.wraps(func)
        def secure_function(*args, **kwargs):
            if user["access-level"] == access_level:
                return func(*args, **kwargs)
            else:
                return f"No access allowed as user is {user['access-level']}."
        
        return secure_function
    
    return decorator

@make_secure("admin")
def getAdminPassword():
    return "adminPass"

@make_secure("guest")
def getUserPassword():
    return "userPass"

print(getAdminPassword())
print(getUserPassword())