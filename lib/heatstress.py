# first draft

import pandas as pd
pd.set_option('display.max_columns', 30)
pd.set_option('display.min_rows', 100)
pd.set_option('display.width', 800)
pd.set_option('display.max_colwidth', 20)


# Read data Sheet 1 then all other sheets in acidbu22.xlsx
filenm = "/home/g/PyCharm/PythonHeatStress/Data/acidbu22.xlsx"
df = pd.read_excel(filenm, sheet_name="Sheet1")
mydf = {'Sheet1':df}

df = pd.ExcelFile(filenm)
mydf2 = pd.read_excel(df, None, skiprows=2, header=None, na_values=".")
mydf2.pop("Sheet1") # remove Sheet1 - formatted differently
mydf.update(mydf2)  # create a single dictionary value

[mydf[ii].dropna(how='all', inplace=True)  for ii in mydf.keys() ]

print(mydf.keys())
print(mydf['Na'])

print("having trouble adding this to commit")
