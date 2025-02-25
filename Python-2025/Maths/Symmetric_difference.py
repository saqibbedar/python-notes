# Symmetric Difference: Remove all matching elements from both A and B and join the leftover from both A and B into single set. A = {1,2,3} B = {3,4,5}, here matching is 3 in both AB so remove it and C={1,2,4,5} is the symmetric difference result

def sym_diff(A,B):
    temp = []
    for a in A:
        if (not a in B):
            temp.append(a)

    return set(temp)

A = {1,2,3}
B = {3,4,5}

print(sym_diff(A,B))