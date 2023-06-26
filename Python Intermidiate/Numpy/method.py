import numpy as np
arr = np.array([8,7,9])
print(arr.argmax()) # It print the index of max element 
print(arr.argmin()) # It print the index of min element 
print(arr.argsort()) # It print the index of array after sort
print(arr.argmin(axis=0)) # It print the index of array which is max in axix=0 
arr1 = np.array([8,2,1])
# a = arr + arr1 # Give sum of matrix
# print(a)
b = np.sqrt(arr) # Take under root
print(b)
arr.max()
arr.min()
arr.sum() 

np.where(arr1>5) # print the matrix place and it give tuple
s = np.count_nonzero(arr1) # Print the count of non zero value
print(s)