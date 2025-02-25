def power_set(listA):
    # Remove duplicates first
    unique_list = list(set(listA))
    n = len(unique_list)
    power_set_size = 2**n
    result = []
    
    # Generate each subset using binary numbers
    for i in range(power_set_size):
        subset = []
        for j in range(n):
            if (i & (1 << j)):
                subset.append(unique_list[j])
        result.append(subset)
    
    return result

A = [1, 2, 3, 4, 4, 4]
print(power_set(A))

        