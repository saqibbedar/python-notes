def set_union(A,B):
    temp = list(A) + list(B)
    return set(temp)

A = {1,2}
B = {3,4}

print(set_union(A,B))