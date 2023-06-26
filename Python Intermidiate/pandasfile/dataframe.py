import numpy as np
import pandas as pd
mydict = {
    'Name' : ['Subhash', 'Dippu', 'Chandan', 'Shikha'],
    'Marks' : [90,98,65,98],
    'City' : ['Delhi', 'South', 'South Delhi', 'South East']
}
df = pd.DataFrame(mydict)
# df.to_csv('dataFrame_index_false.csv',index=False)
# df.to_csv('dataFrame.csv')
# print(df.head(2)) # Print first two rows
# print(df.tail(2)) # Print last two rows
# print(df.describe()) # Print everthing about the numerical values like percentage, max, min etc

# read = pd.read_csv('dataFrame_index_false.csv') # Open file and read
# print(read)

# print(read['Marks']) # You get only Marks column

# print(read['Marks'][1]) # It work as matrix

# df['Marks'][1] = 78 # You can copy of a slice from a DataFrame it can not change in man data
# print(read )

# df.to_csv('dataFrame_index_false.csv')
# print(df)

# df.index = ['First', 'Second', 'Third','Four'] # It will change the value directly
# print(df)

ser = pd.DataFrame(np.random.rand(333,4)) # It will provide you the randam dataframe of data
print(type(ser))
print(ser)

# print(ser.index)
print(ser.T) # Transpose