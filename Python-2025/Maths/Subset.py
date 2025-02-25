# def is_subset(setA, setB):
#     if(len(setA) > len(setB)):
#         return False
#     for x in setA:
#         if(not x in setB):
#             return False
#     return True

# A = [1,2,3]
# B = [1,2,3,4]

# print(is_subset(A, B))

# using set

def is_subset(A,B):
    if(len(A)>len(B)):
        return False
    for x in A:
        if(not x in B):
            return False
    return True            

setA = {1,2,2}
setB = {1,2,3}

print(is_subset(setA, setB))

print(setA.issubset(setB))