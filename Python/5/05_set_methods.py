# Creating an empty set
b = set()
print(type(b))

## Adding values to an empty set
b.add(4)
b.add(4)
b.add(5)
b.add(5) # Adding a value repeatedly does not changes a set
b.add((4, 5, 6)) # We can insert tuple because we cann't change

# Hashable -> Means we cann't change the value e.g int , float , str , tuple and NoneType.
# Unhashable -> Means we can change the value e.g list 

## Accessing Elements
# b.add({4:5}) # Cannot add list or dictionary to sets
print(b)

## Length of the Set
print(len(b)) # Prints the length of this set

## Removal of an Item
# b.remove(5) # Removes 5 from set b
# b.remove(15) # throws an error while trying to remove 15 (which is not present in the set)
# print(b)

print(b.pop()) # It will pop any random number 
print(b)