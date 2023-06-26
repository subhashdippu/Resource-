import numpy as np
import sys
arr1 = [2,5,6]
arr = np.array(arr1)
a = sys.getsizeof(1) * len(arr1)
print(a)
b = arr.itemsize * arr.size # Hence numpy array take less space then list
print(b)
# scipy.org