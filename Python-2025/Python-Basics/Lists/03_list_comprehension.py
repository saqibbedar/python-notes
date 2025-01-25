# Syntax for list comprehension
# [expression for item in iterable if condition]

# expression: The value to be added to the list, after each iteration or passing test if we have condition
# item: The variable that takes the value of the current element from the iterable.
# iterable: The collection of items to iterate over (e.g., a list).
# condition (optional): A filter that selects which items to include in the new list.

my_list = [1,2,3,4,5,6]

filtered_list = [x for x in my_list if x % 2 == 0]
print(filtered_list)

# The above expression is equivalent to:
filtered_list_1 = []
for x in my_list:
    if x % 2 == 0:
        filtered_list_1.append(x)

print(filtered_list_1)
