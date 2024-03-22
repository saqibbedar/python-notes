# Tuples are same like list(arrays) but the difference is that we can not assign new values to existing elements

'''
    myTuple = (1, 2, 3, 4)
    myTuple[0] = 10 // this will return error as assignment does not work in tuples
'''

myTuple = (1, 2, 3, 4, 5)
tuple_Length = len(myTuple)
print(myTuple, "\n", tuple_Length, type(myTuple)) 

# it can be used on strings
str_tuple = ("Saqib", "Haider", "Ahmed", "Ali")
print(str_tuple)

# we can also combine different data types together 
combine_tuple = (1, 3, "Hello", True, "hey", 332, 32, False)
print(combine_tuple, '\n' ,len(combine_tuple), '\n', type(combine_tuple))