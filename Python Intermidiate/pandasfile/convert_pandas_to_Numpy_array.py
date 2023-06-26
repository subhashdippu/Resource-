import numpy as np
import pandas as pd
ser = pd.DataFrame(np.random.rand(333,4)) # It will provide you the randam dataframe of data
# print(type(ser))
# print(ser)

print(type(ser))
print(ser.to_numpy()) # Numpy array
print(ser[0]) # Print one column


print(ser[0].isnull()) # If the value is null in column the it print true overthere else false
ser[1] = 0 # zero the given column
ser.loc[:,[1]] = 54 # This is good practice because it will change the data in main dataframe
print(ser)