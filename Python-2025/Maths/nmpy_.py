import numpy as np

# 1. Array Creation
arr1 = np.array([1, 2, 3])               # Create array
zeros = np.zeros((3, 3))                 # Array of zeros
ones = np.ones((2, 2))                   # Array of ones
range_arr = np.arange(0, 10, 2)          # Range array
linspace = np.linspace(0, 1, 5)          # Evenly spaced numbers
random_arr = np.random.rand(3, 3)        # Random array
identity = np.eye(3)                     # Identity matrix

# 2. Array Operations
arr2 = arr1 * 2                          # Element-wise multiplication
arr3 = arr1 + arr2                       # Element-wise addition
dot_product = np.dot(arr1, arr2)         # Dot product
concatenated = np.concatenate([arr1, arr2]) # Concatenate arrays

# 3. Math Functions
exp = np.exp(arr1)                       # Exponential
log = np.log(arr1)                       # Natural log
sqrt = np.sqrt(arr1)                     # Square root
sin = np.sin(arr1)                       # Sine
cos = np.cos(arr1)                       # Cosine

# 4. Statistics
mean = np.mean(arr1)                     # Mean
median = np.median(arr1)                 # Median
std = np.std(arr1)                       # Standard deviation
var = np.var(arr1)                       # Variance
max_val = np.max(arr1)                   # Maximum
min_val = np.min(arr1)                   # Minimum

# 5. Matrix Operations
transpose = arr1.T                       # Transpose
reshape = arr1.reshape(3, 1)             # Reshape array
stack = np.vstack([arr1, arr2])          # Vertical stack
hstack = np.hstack([arr1, arr2])         # Horizontal stack

# 6. Array Manipulation
sort = np.sort(arr1)                     # Sort array
unique = np.unique(arr1)                 # Unique elements
where = np.where(arr1 > 2)               # Find indices where condition is true
mask = arr1 > 2                          # Boolean masking
split = np.split(arr1, 3)                # Split array