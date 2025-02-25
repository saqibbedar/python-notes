def set_intersection(A,B):
    temp = []
    for a in A:
        if(a in B):
            temp.append(a)
    return set(temp)

print(set_intersection({1,2,3},{1,3,5,7}))