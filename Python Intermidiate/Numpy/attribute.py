import numpy as np
x = [[2,5,6], [1,4,3], [8,7,9]]
arr = np.array(x)
arr.T # Transpose the element
print(arr)

arr.flat # it make the iterator
for i in arr.flat:
    print(i)
arr.ndim # print Dimection of array
arr.size # Size of array
arr.bytes # Total bites consume