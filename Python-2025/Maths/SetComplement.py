# Ac contains all elements not in A, relative to universal set U

def set_complement(U,A):
    temp = []
    for x in U:
        if(not x in A):
            temp.append(x)
    return set(temp)

U = {1,2,3,4,5}
A = {1,2}
print(set_complement(U, A)) # Ac = {3,4,5} as A contains {1,2} and Ac contains only values which are not occupied by A
