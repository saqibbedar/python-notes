def cartesian_product(A, B):
    result = []
    for a in A:  # Iterate over the first set
        for b in B:  # Iterate over the second set
            result.append((a, b))  # Append tuple (a, b) to the result list
    return result


A = ["a", "b"]
B = [1,2]

print(cartesian_product(A,B))
