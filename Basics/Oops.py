
# Class basics
print("\n\tClass Basics\n")

class MyClass():

    # Constructor
    def __init__(self,constructorArg: str) -> None:

        '''
            Attributes:
                We take in arguments from constructor.
                Assign it to a new variable
                    self.newVariable = argument
                where the new variable's name will be "newVariable" itself.

                This means assignment and creation of variable are done 
                in the same line, saving us extra line of code.

                These variables are also called attributes.
        '''
        self.constructorArgAttribute = constructorArg

        print(f"Class created with code: {constructorArg}")

    # Destructor. Can be called if we do `del MyClass`.
    def __del__(self):
        print("MyClass deleted.")

    # Methods

    def fun(self): 
        '''     
        We are declaring self here to get the instance of the class itself.
        Python automatically passes self as the first argument when this function is called.
        '''
        print("MyClass's fun method executed.")

    def __fun(self):
        '''
        Private methods start with __ and look like __functionName.
        '''
        print("Private method called.")

    def callPrivateMethod(self):
        self.__fun()


my_class = MyClass(constructorArg = "Class Basics")
print(my_class.constructorArgAttribute)
my_class.fun()
my_class.callPrivateMethod()

print(f"\nType of my_class variable is {type(my_class)}")     # class "__main__.MyClass"


# Inheritance
print("\n\tInheritance \n")

class MyInheritedClass(MyClass):
    
    def __init__(self, constructorArg: int) -> None:
        super().__init__(constructorArg)

    # Override methods
    def fun(self):
        print("Overriden Method executed.")


my_inherited_class = MyInheritedClass("Inheritance")
print(my_inherited_class.constructorArgAttribute)
my_inherited_class.fun()

# Polymorphism
print("\n\tPolymorphism\n")

'''
    Consider two classes Dog and Cat. Usually when we have some methods 
    which have same name, we can call those methods if we know that the 
    variable is of type either Dog or Cat, we can call the common name 
    function without even enquiring the type of the variable which has 
    the instance of the class stored.
'''

class Dog():
    def speak(self):
        print("Barks")

class Cat():
    def speak(self):
        print("Meows")

def petSpeaks(pet):
    pet.speak()

my_pet = Dog()
petSpeaks(my_pet)

my_pet = Cat()
petSpeaks(my_pet)

# Abstract class

# We raise error whenever our speak method is called without implementation.
class Animal():

    def __init__(self) -> None:
        pass

    def speak():
        raise NotImplementedError("Subclass must implement this function.")
    
# Special methods

class Book():
    
    def __init__(self, title: str, author: str, pages: int) -> None:
        self.title = title
        self.author = author
        self.pages = pages

    # This is a magic method.
    def __str__(self) -> str:
        '''
        Magic methods are used to give a representation of the corresponding
        class when used in predefined functions like print().

        If we call `print(Book("a","b"))` we will get something like `<__main__.Book object at 0x0000019d848d94c0>`.

        To solve this issue, we use this __str__ method which gives us string representation of our class Book.
        '''
        return f"Book title: {self.title}, author: {self.author}"
    
    def __len__(self):
        return self.pages

my_book = Book("James","Potter",155)

print(my_book)   # Prints: "Book title: James, author: Potter"

print(len(my_book))     # Or use my_book.__len__()

# Delete variables

del my_book
# print(my_book)      # Prints: "name 'my_book' is not defined"

print("\n\n\n\t@classmethod and @staticmethod\n")

# @classmethod and @staticmethod

class classTest:

    classVariable = "ClassVariable"

    def instance_method(self):
        '''
        These can only be called with instantiation of the class.
        This means, init will be called unnecessarily if we just want to use this method only.
        Takes instance of the parent class object as the first argument (self).
        Eg: classTest().instance_method()
        '''
        print(f"Instance method called of {self}")
        print(self.classVariable)

    @classmethod
    def class_method(cls):
        '''
        These can be called with or without the instantiation of the class.
        Takes the class itself as the first argument (cls).
        Eg: classTest.class_method()
        '''
        print(f"Class method called of {cls}")
        print(cls.classVariable)

    @staticmethod
    def static_method():
        '''
        Same as class method, but doesn't take any strict first argument.
        Eg: classTest.static_method()
        '''
        print(f"Static method called.")
        print("Cannot access class variable.")

classTest().instance_method()
print()
classTest.class_method()
print()
classTest.static_method()

print("\n\n")
