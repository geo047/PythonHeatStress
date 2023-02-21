# first draft

import myplots as myplt
import pandas as pd
#import matplotlib.pyplot as plt
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



## Construct dataframe for plotting means

df = mydf.groupby(['Sample','treatment'])['sodium'].mean().to_frame(name='mean').reset_index()
df.columns = ['CollDay','Diet','Mean']


df = df.pivot(columns='Diet',  index='CollDay', values='Mean')
print("in here")
print(df.head())

myplt.my_plot(df=df, ylab='mean sodium level')



#mydfplt = mydf.pivot(index='Sample', columns='ID', values='sodium')
#mydfplt.sort_values(by='Sample', inplace=True)

#print(mydfplt.head(5))

#mydfplt.plot(kind="line")
#plt.show()

