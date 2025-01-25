my_list = [1, 2, 3, 4, 5, 6]

# using filter() with lambda function
filtered_list = list(filter(lambda x: x % 2 == 0, my_list))
print(filtered_list) # output: [2, 4, 6]

from functools import reduce

# Using reduce() to sum all elements
sum_of_elements = reduce(lambda x, y: x + y, my_list)
print(sum_of_elements)  # Output: 21

# List comprehension with condition
filtered_list_2 = [x for x in my_list if x % 2 == 0]
print(filtered_list_2)  # Output: [2, 4, 6]

# any(): Returns True if any element of the iterable is true.
# all(): Returns True if all elements of the iterable are true.
print(any(x > 5 for x in my_list))  # Output: True
print(all(x > 0 for x in my_list))  # Output: True

# Equivalent program for any
result = False
for x in my_list:
    if x > 5:
        result = True
        break
print(result)

# Equivalent program for all
result = True
for x in my_list:
    if not (x > 0):
        result = False
        break
print(result)