import numpy as np

def matrix_mul(A,B):
    return np.dot(A,B)

def matrix_add(A,B):
    return A + B

def matrix_sub(A,B):
    return A - B

def matrix_transpose(A):
    return A.T # transpose

def matrix_inverse(A):
    return np.linalg.inv(A)

A = np.array([[1,2], [3,4]])
B = np.array([[5,7], [3,4]])

print(matrix_mul(A,B))
print(matrix_add(A,B))
print(matrix_sub(A,B))
