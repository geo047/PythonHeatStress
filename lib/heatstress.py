# first draft

import myplots as myplt
import pandas as pd
import numpy as np
#import seaborn as sns
import matplotlib.pyplot as plt
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
mydf = mydf.astype( {'ID':'string', 'Sample':'int', 'treatment':'string'}  )
mydf['treatment'].replace({'trt_1':'diet I', 'trt_2':'diet II','trt_3':'diet III'}, inplace=True)


## Construct dataframe for plotting means
#df = mydf.groupby(['Sample','treatment'])['sodium'].mean().to_frame(name='mean').reset_index()
#df.columns = ['CollDay','Diet','Mean']
#df = df.pivot(columns='Diet',  index='CollDay', values='Mean')
#print(df.head())

cols = mydf.columns.values
cols= np.delete( cols, [0,1,2,3] )  # trait names from columns of dataframe
fig = plt.figure()
fig.subplots_adjust(hspace=0.4, wspace=0.4)
ax = fig.add_subplot(2, 2, 1)
plot1 = myplt.my_plot(df=mydf, traitnme='sodium')
ax = fig.add_subplot(2, 2, 2)
plot1 = myplt.my_plot(df=mydf, traitnme='sodium')
ax = fig.add_subplot(2, 2, 3)
plot1 = myplt.my_plot(df=mydf, traitnme='sodium')
ax = fig.add_subplot(2, 2, 4)
plot1 = myplt.my_plot(df=mydf, traitnme='sodium')


plt.show()

