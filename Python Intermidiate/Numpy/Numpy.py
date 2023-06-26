import numpy as np
# You can decide the size of e lement like np.int8 
# Creating the numpy array
# method 1
myArr = np.array([[2,54,6,1]],np.int8) 
# method 2 with fucton 
zeros = np.zeros((2,5))
print(zeros)
rng = np.arange(15)
print(rng)
isSpace = np.linspace(1,50,10) # Give no with equal differnce from 1 to 50 and give total 10 number
print(isSpace)
empt = np.empty((5,6)) # Give empty array
print(empt)
empt_like = np.empty_like(isSpace) # create empty Array with size of isSpace
print(empt_like)
# np.identitiy(54) It Create identitity matrix
# arr.reshape(3,5) Arrange with this matrix
# arr.ravel() Arrange in a single array

print(myArr)
print(myArr.shape) # Print how many row and colum
print(myArr.dtype) # Print the type you asigned like int8