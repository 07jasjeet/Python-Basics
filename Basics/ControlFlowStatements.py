
hashNum = 1
def addSpace():
    global hashNum
    print(f"\n\n#{hashNum}")
    hashNum += 1

addSpace()
#1 If else statements.
myBool = False

if myBool:
    print("if")
elif not myBool:
    print("elif")
else:
    print("else")

addSpace()

# For loops

myList = [1,2,3,4,5]

#2 iterate with list item
for item in myList:
    print(item, end=" ")

addSpace()

#3 Range: Generates LIST of numbers with specified parameters. Used to iterate with loop count.
#  Range(start, end, step)
for i in range(0,5,2):
    print(i, end=" ")

addSpace()

#4 Iterate with each list item, but also have full control of list item.
# This is called tuple unpacking.
myTupleList = [(1,2), (3,4), (4,5), (5,6)]

for (a, b) in myTupleList:
    print(a, end=" ")

addSpace()

# Iterating with dictionaries.
myDict = {'k1': 1, 'k2':2, 'k3':3}


#5 Prints keys only by default.
for item in myDict:
    print(item, end=" ")

addSpace()

#6 Prints values only.
for item in myDict.values():
    print(item, end=" ")

addSpace()

#7 Have both key and value avaliable while looping.
for key, value in myDict.items():
    print(key, end=":")
    print(value)

addSpace()

# While loop
while 1==2:
    # Do something
    1

# Pass keyword lets us skip definition of loop without any compiler errors.
# Pass does nothing.
for i in range(5):
    pass

#8 Continue keyword skips the current iteration and moves on to next.
print(f"Original list: {myList}\nWith continue: ", end="")
for item in myList:
    if item == 2:
        continue
    print(item, end=" ")

# Break works as expected.

addSpace()

#9 Loop with index
for index, item in enumerate(myList):
    print(f"Index: {index}, Item = {item}")

addSpace()

#10 Zip function: Creates TUPLES of all LIST's items at same index.
list1 = [1,2,3,4,5,6,7,8]
list2 = ['a','b','c']
list3 = [100,200,300]

for item in zip(list1,list2,list3):
    print(item)

addSpace()

#11 `in` keyword
print(2 in myList)

addSpace()

#12 List comprehnshions
myString = "Hello"
stringList = [letter for letter in myString]    # We are basically just appending.

print(stringList)

# This also gives us some flexibility.
print( [element**2 for element in myList] )
print( [x for x in range(0,20) if x%2 == 0] )

nestedLoopList = [x*y for x in myList for y in list1]