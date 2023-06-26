import numpy as np
import pandas as pd

mydict = {
    'Name' : ['Subhash', 'Dippu', 'Chandan', 'Shikha'],
    'Marks' : [90,98,98,67],
    'City' : [np.NaN ,np.NaN, np.NaN , np.NaN]
}
df = pd.DataFrame(mydict)
ser = pd.DataFrame(np.random.rand(333,4)) # It will provide you the randam dataframe of data

ser.columns = list("ABCD")
# print(ser.head(2))
# ser = ser.drop('A',axis=1) # Drop column A
# print(ser.head(2))

# ser.drop( ['A','D'], axis=1,inplace=True) # Here it will delete the column directly to the main data
# print(ser.head(3))

# ser.reset_index(drop=True,inplace=True) # Reset the index

# df.dropna()
# print(df.dropna(how='all', axis=1)) # It will remove NaN

# dub = df.drop_duplicates(subset='Marks') # It will remove dublicate from the Marks 
# print(dub)

dub = df.drop_duplicates(subset=['Marks'], keep='last') # It will not remove the dublicate from only last
print(dub)

# dub = df.drop_duplicates(subset=['Marks'], keep=False) # All dublicates will remove 
# print(dub)

print(df.info()) # It will give the all information from df