# Remove all elements matching elements and return the remaining one, if A-B then check all A's elements in B and hold the not matched in temp list and return the list as a set

def set_diff(A,B):
    temp = []
    for x in A:
        if(not x in B):
            temp.append(x)

    return set(temp)

A = {1,2,3,4}
B = {1,3}

print(set_diff(A,B))