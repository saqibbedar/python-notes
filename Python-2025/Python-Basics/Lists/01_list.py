# List is a collection of items that are ordered and changeable. It is same as vectors in cpp and arrays in javascript, just name is different.

# list creation
my_list = [1, 2, 3, 4, 5]

print(my_list[0]) # output: 1
print(my_list[-1]) # output: 5 (last element)

# Modifying list elements
my_list[0] = 10
print(my_list[0]) # output: 10

# List methods

# append(): Adds an element at the end of the list.
my_list.append(6)

# insert(): Adds an element at the specified position.
my_list.insert(1, 15)

# remove(): Removes the first item with the specified value.
my_list.remove(10)

# pop(): Removes the element at the specified position (or the last item if no index is specified).
my_list.pop()
my_list.pop(1)

# clear(): Removes all the elements from the list.
my_list.clear()

# index(): Returns the index of the first element with the specified value.
my_list.index(3)

# count(): Returns the number of elements with the specified value.
my_list.count(3)

# sort(): Sorts the list.
my_list.sort()

# reverse(): Reverses the order of the list. 
my_list.reverse()

# extend(): Adds the elements of a list (or any iterable) to the end of the current list.
my_list.extend([7, 8, 9])

# List comprehension: it provides a concise way to create lists.
squares = [x**2 for x in range(10)]

# Slicing: You can access a range of elements in a list by using slicing.
sub_list = my_list[1:3]  # Elements from index 1 to 2

# Iterating
for item in my_list:
    print(item)