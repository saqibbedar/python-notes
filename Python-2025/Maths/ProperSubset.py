# def is_proper_subset(setA, setB):
#     if(setA == setB):
#         return False
#     for x in setA:
#         if(not x in setB):
#             return False
#     return True

# A = [1,2,3]
# B = [1,2,3]

# print(is_proper_subset(A,B))


"""
def is_proper_subset(setA, setB):
    return setA != setB and all(x in setB for x in setA)

A = [1, 2, 3]
B = [1, 2, 3]

print(is_proper_subset(A, B))
"""

# Using sets data structure
def is_proper_subset(setA, setB):
    if(setA == setB):
        return False
    for x in setA:
        if(not x in setB):
            return False
    return True

A = {1,2,3,4}
B = {1,2,3,4,5}

print(is_proper_subset(A,B))