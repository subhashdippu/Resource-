import numpy as np
import pandas as pd
data = pd.read_excel('data.xlsx', sheet_name='Sheet') # This will open the sheet the we can perform a certain task
data.iloc(0,0) = 54
data.to_excel('data.xlsx', sheet_name='Sheet') # Here you can save the change