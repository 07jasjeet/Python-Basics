
myList = ['hello', 5 , 1.22334]

# Slicing and indexing same as strings
myList[1:] # prints [5, 1.22334]

# Lists are mutable, unlike strings which do 
# not let us change individual letters.
myList[0] = 'Hello world'

# Append
myList.append(True)     # Increases size of list and adds to last index.

# Removes  item and return it.
print(myList.pop())     # Pop last item
print(myList.pop(2))    # Pop at index 2

# Sorting
newList = ['a', 'e', 'x', 'b', 'c']

newList.sort()
print(newList)

# Multiplying list
multipliedList = myList*3

print(multipliedList)