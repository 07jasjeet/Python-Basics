
myString = "Hello world"

# Get size of the string.
len(myString)

# Get char at index, negative index 
# means py will start from behind.
myString[-1]    # This gets last char of the string.
"Hello world"[3]    # Gives char at index 3.

# Substring after x (Included)
myString[5:]

# Substring before x (excluded)
myString[:5]

# Substring between x (included) and y (excluded).
myString[5:8]

# Substring with adjacent chars at constant distance.
myString[::2]

# Same as above but with starting index (included).
myString[5::2]

# Same as above but with ignore index case in between. All characters after ignore index (included) are ignored.
myString[3:7:2]

# Reverse a string using slicing
myString[::-1]

# String formatting
print( "The {1} {2} {0}.\n".format("fox","quick","brown") )
print( "The {0} {0} {0}.\n".format("fox","quick","brown") )
print( "The {q} {b} {f}.\n".format(f = "fox", q = "quick", b = "brown") )

# Float formatting "{value:width.precision}"
# Width adds whitespaces in front if the number to be displayed has smaller length (in string sizes) than the specified width. 
# Example: 7.77 has width 4. Width of 5 would add a whitespace.
myFloat = 1234567.7654321
print("My result is {f:10.1}.".format(f = myFloat))

# String formatting type 2
print(f"\nMy result is {myFloat}\n")