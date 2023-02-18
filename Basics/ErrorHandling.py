def divide(a: int, b: int):
    return a/b

def exceptionHandlingOne():
    try:
        # Try block
        a = divide(1,5)

        # OS error as file mode was read but we tried to write to it.
        with open("f:\\Python Programing\\Basics\\test.txt", "r") as file:
            file.write("Testwrite")

    except ArithmeticError:            
        # Catch Block                 
        print("Arithmetic error")
    except OSError:
        print("OS error")
    except:
        # All other exceptions are handled by this block.
        print("Some error occurred.")
    else:
        # If no errors were found, this is executed.
        print("else executed.")
    finally:
        # Always executed even if errors are found.
        print("finally executed.")

def exceptionHandlingTwo():
    try:
        myInt = int(input("Enter an int: "))
    except:
        print("Not an Int.")
    finally:
        print("Goodbye")


exceptionHandlingTwo()

# Custom errors
# class CustomErrorName(`Inherit from error of your choice.`):

class CustomError(ValueError):
    pass

def customErrorTrial():
    raise CustomError("Custom Error Raised")

customErrorTrial()