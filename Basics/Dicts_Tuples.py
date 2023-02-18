
# Dictionary
myDict = {'key':'value', 'key0':'value0'}
print(f"\n{myDict}\n")

print(myDict.keys())

print(myDict.values())

# Tuples
# Same as list, but they are immutable and use () instead of [].
myTuple = (1,1,2,3)

myTuple.count(1)    # Returns number of times 1 has occured.

# Sets  Immutable
# -> Unique collection of items
# -> Immutable
# -> Property getter (mySet[1]) doesn't work. 
mySet = set()
mySet.add(1)
mySet.add(2)
mySet.add(3)

# Get a set from a list or tuple.
listSet = set()
listSet = [myTuple]
print(listSet)