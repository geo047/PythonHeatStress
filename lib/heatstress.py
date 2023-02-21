# first draft

import pandas as pd
pd.set_option('display.max_columns', 30)
pd.set_option('display.min_rows', 100)
pd.set_option('display.width', 800)
pd.set_option('display.max_colwidth', 20)


# Read data sheets
filenm = "/home/g/PyCharm/PythonHeatStress/Data/acidbu22.xlsx"
mydf = pd.read_excel(filenm, sheet_name='Sheet1',
                      na_values=".")
mydf.columns = mydf.columns.str.strip() # remove pesky spaces in col names
print(mydf.columns)
mydf.sort_values(by=['ID', 'Sample_Date', 'treatment'], inplace=True)
print(mydf.head(15))
exit()

# get sheets in correct shape
for ii in mydf2.keys():
    mydf2[ii].columns = ['diet', 'id', 'room','pen', 'd45', 'd50', 'd54',
                         'd57','d58','d59','d60','d61','d62','d64','d66','d68',
                         'd70','d76','d81','d88']

    print(mydf2[ii].head())
    exit()
    mydf2[ii].dropna(how='all', inplace=True)  # removing entire rows of NaN
    mydf2[ii] = pd.melt(mydf2[ii], id_vars=['diet','id','room','pen'])  # reshape
    mydf2[ii] = mydf2[ii].rename({'variable':'day', 'value':'y'}, axis=1)
    mydf2[ii].sort_values(by=['id', 'day'], inplace=True)

    convert_dict = {'diet' : 'string',
                      'id' : 'string',
                      'room' : 'string' ,
                      'pen' : 'string',
                      'day' : 'string',
                      'y' : 'float'}
    mydf2[ii] = mydf2[ii].astype(convert_dict)
# melt into shape

print(mydf2['Na'])
exit()

mydf.update(mydf2)  # add Sheet1 to other sheets in mydf
[mydf[ii].dropna(how='all', inplace=True)  for ii in mydf.keys() ]  # reading all sheets

print(mydf.keys())
print(mydf['Na'])

print("having trouble adding this to commit")

