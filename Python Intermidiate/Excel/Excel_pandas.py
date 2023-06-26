import pandas as pd
file = pd.ExcelFile("/Users/Subhash/Downloads/sales.xlsx")
print(file.sheet_names)
sheet = file.parse("sales")