# Read in raw data, modify, transform,
# and output

import pandas as pd
import numpy as np




# Read data sheets
filenm = "/home/g/PyCharm/PythonHeatStress/Data/acidbu22.xlsx"
mydf = pd.read_excel(filenm, sheet_name='Sheet1',
                      na_values=".")
mydf.columns = mydf.columns.str.strip() # remove pesky spaces in col names
mydf.sort_values(by=['ID', 'Sample_Date', 'treatment'], inplace=True)
mydf = mydf.astype( {'ID':'string', 'Sample':'int', 'treatment':'string'}  )
mydf['treatment'].replace({'trt_1':'diet I', 'trt_2':'diet II','trt_3':'diet III'}, inplace=True)
# remove rows with these dates 2022-09-22, and after 17/10
mydf.query('~(Sample_Date=="2022-09-22" or Sample_Date > "2022-10-17") ', inplace=True)
mydf.Sample -= 1 # reindexing Sample day number to start from 1.


# create Event column
conditions = [
    mydf.Sample_Date <= '2022-10-01',
    (mydf.Sample_Date > '2022-10-01') & (mydf.Sample_Date <= '2022-10-08'),
    mydf.Sample_Date > '2022-10-08'
]

values = ['PreHeat', 'Heat', 'Recovery']
mydf['Event'] = np.select(conditions, values, default=None)
#print(mydf.groupby('Event').count()) #  the numbers check out.

mydf.to_csv('/home/g/PyCharm/PythonHeatStress/Data/cleanedData.csv', index=False)
