# first draft

import myplots as myplt
import pandas as pd
import numpy as np
#import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib
#from matplotlib.backends.backend_pgf import FigureCanvasPgf
#matplotlib.backend_bases.register_backend('pdf', FigureCanvasPgf)


pd.set_option('display.max_columns', 30)
pd.set_option('display.min_rows', 100)
pd.set_option('display.width', 800)
pd.set_option('display.max_colwidth', 20)


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
mydf = mydf.astype({"Sample": 'category'})


## CK
print(mydf.treatment.unique())
print(mydf.query('treatment == "diet I"' ).groupby(['treatment','Sample'])['CK'].mean())
exit()




cols = mydf.columns.values
cols= np.delete( cols, [0,1,2,3] )  # trait names from columns of dataframe

print(len(cols))

fig = plt.figure()
fig.subplots_adjust(hspace=0.6, wspace=0.6)
counter = 0
for ii in cols[0:9]:
    counter += 1
    ax = fig.add_subplot(3, 3, counter)
    p = myplt.my_plot(df=mydf, traitnme=ii)
plt.savefig('multiplotfig1.pdf')


fig = plt.figure()
fig.subplots_adjust(hspace=0.6, wspace=0.6)
counter = 0
for ii in cols[0:9]:
    counter += 1
    ax = fig.add_subplot(3, 3, counter)
    p = myplt.my_plot(df=mydf, traitnme=ii)
plt.savefig('multiplotfig1.pdf')


fig = plt.figure()
fig.subplots_adjust(hspace=0.6, wspace=0.6)
counter =0
for ii in cols[9:18]:
    counter += 1
    print(counter)
    ax = fig.add_subplot(3, 3, counter)
    p = myplt.my_plot(df=mydf, traitnme=ii)
plt.savefig('multiplotfig2.pdf')

fig = plt.figure()
fig.subplots_adjust(hspace=0.6, wspace=0.6)
counter = 0
for ii in cols[18:25]:
    counter += 1
    ax = fig.add_subplot(3, 3, counter)
    p = myplt.my_plot(df=mydf, traitnme=ii)
plt.savefig('multiplotfig3.pdf')



#plt.show()

