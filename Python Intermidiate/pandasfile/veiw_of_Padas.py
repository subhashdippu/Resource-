import numpy as np
import pandas as pd
ser = pd.DataFrame(np.random.rand(333,4)) # It will provide you the randam dataframe of data
# print(type(ser))
# print(ser)
da = ser # Here it will work as View like a pointer
da[0][0] = 545 # It will change the value of ser. it get create a problem with view sometime in view it shows or sometime not show 
# print(ser)

da = ser.copy() # It will copy the data from ser to da
ser.loc[0][0] = 45
print(ser.head(2)) # It will change the data for view and in original 

ser.columns = list("ABCD")
print(ser.head(2))

print(ser.loc[[1,2],['A','B']]) # It will just print the given column and row
print(ser.loc[:,['A','B']]) # It will just print the given column and all row