import numpy as np
x = [[2,5,6], [1,4,3], [8,7,9]]
arr = np.array(x)
print(arr)
print(arr.sum(axis=0)) # Print sum of all rows
print(arr.sum(axis=1)) # Print sum of all collum  