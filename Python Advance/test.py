# # import matplotlib.pyplot as plt 
# # x = [2,3,4,5,6]
# # y = [120,356,400,963,100]
# # plt.plot(x,y) # This is going to plot the graph by given list
# # plt.show()    # This is going to show the ploted graph by the given list in GUI


# # leg = ["Jan", "Feb", "March", "April"]
# # plt.xticks(x, leg) # This is going to replace the numeric value of x axis into string
# # plt.plot(x,y)
# # plt.show()
# import numpy as np
# import pandas as pd
# data = pd.read_excel('salary.xlsx', sheet_name='salary.xlsx') # This will open the sheet the we can perform a certain task
# # data.iloc(0,0) = 54
# data.to_excel('data.xlsx', sheet_name='Sheet') # Here you can save the change

import numpy as np
import pandas as pd
mydict = {
    'Name' : ['Subhash', 'Dippu', 'Chandan', 'Shikha'],
    'Marks' : [90,98,65,98],
    'City' : ['Delhi', 'South', 'South Delhi', 'South East']
}
df = pd.DataFrame(mydict)
# print(df)
# df.to_csv('dataFrame_index_false.csv',index=False)
df.to_csv('dataFrame.csv')
# print(df.head(2)) # Print first two rows