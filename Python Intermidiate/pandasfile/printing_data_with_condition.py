import numpy as np
import pandas as pd
ser = pd.DataFrame(np.random.rand(333,4)) # It will provide you the randam dataframe of data


ser.columns = list("ABCD")

print(ser.loc[[1,2],['A','B']]) # It will just print the given column and row
print(ser.loc[:,['A','B']]) # It will just print the given column and all row
print(ser.loc[(ser['A']<0.3) & (ser['C']>0.1)])

# Print value with index view
print(ser.iloc[0,3])
print(ser.iloc[[0,3],[1,2]]) # It print row 0 and 3 and column 1 and 2