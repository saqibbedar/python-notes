# List tutorial for beginners in python
# Lists in Python are similar to arrays in other programming languages. They are used to store multiple items in a single variable. Lists are ordered, changeable, and allow duplicate values.

# basic numbers list
num = [1, 3, 5, 7]
print(num) # print list
print(num[-1]) # print last value of list


# List length
# We can use builtin `len()` function to determine the length of list or apply method list `__len__()`
length = len(num)
print("Length of the list using len():", length)
length = num.__len__()
print("Length of the list using __len__():", length)


# Concatenation +
# python supports concatenation, meaning there by we can add two lists using
num += [9, 11, 13] # adding new elements to list
print(num)

# Simple assignment in Python never copies data. When you assign a list to a variable, the variable refers to the existing list.
num = [1, 3, 5, 7, 9, 11, 13, 15, 17]
newNumList = num
newNumList.append(19) # append method is used to add value in at last index of list

if newNumList == num:
    print(True, newNumList)
else:
    print(False, newNumList)


# Creating a Shallow Copy of a List
# We can use the `[:]` syntax to create a shallow copy, but it refers to a separate object. This means that modifications made to the shallow copy won't modify the original list. However, it is better to use the `copy` module as it is helpful for complex data structures or nested lists.
originalList = [1, 2, 3, 4, 5]
shallow_copy = originalList[:]

print(f'originalList: {originalList}')
print(f"shallow_copy: {shallow_copy}")

shallow_copy.append(6)

print(f'originalList: {originalList}')
print(f"shallow_copy: {shallow_copy}")


# DeepCopy of List
# We can use built-in `copy` module to deeply copy a list 
import copy
num = [1,2,3]
newNumList = copy.deepcopy(num)
newNumList.append(4)
print("NewNum List Length: ",newNumList.__len__(), "and List elements: ", newNumList)
print("Num List Length: ",num.__len__(), "and List elements", num)

# Assignment Slice
# Assignment to slices is also possible, and this can even change the size of the list or clear it entirely:
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(letters)

# replace some values
letters[2:5] = ['C', 'D', 'E']
print(letters)

# now remove them
letters[2:5] = []
print(letters)

# clear the list by replacing all the elements with an empty list
letters[:] = []
print(letters)

