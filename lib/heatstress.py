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
#mydf = mydf.astype({"Sample": 'category'})



## CK
#print(mydf.treatment.unique())
#print(mydf.query('treatment == "diet I"' ).groupby(['treatment','Sample'])['CK'].mean())





cols = mydf.columns.values
cols= np.delete( cols, [0,1,2,3] )  # trait names from columns of dataframe

# This is clunky but for some reason, the first time plt.figure is called,
# the first plot in the panel has incorrect font size (they are huge).
# All the multi-panel plots followingn this are fine. Weird.
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



##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
## One Way Anova of all traits
##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import scipy.stats as stats


for ii in cols:
    #print(mydf.query('treatment == "diet I"'))

    fvalue, pvalue = stats.f_oneway(mydf.query('treatment == "diet I"')[ii],
                                    mydf.query('treatment == "diet II"')[ii],
                                    mydf.query('treatment == "diet III"')[ii],
                                    )
    print(f'Trait = {ii }   F value = {round(fvalue,3)} p-value = {round(pvalue,3)}')



##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
## Repeated Measures within Heat Event
##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# REF: https://pandas.pydata.org/pandas-docs/version/0.22/r_interface.html
# #Exporting a pandas df into R land within python.
# #A working example
# from rpy2.robjects import r, pandas2ri
# import pandas as pd
# pandas2ri.activate()
#
# pd_df = pd.DataFrame({'int_values': [1,2,3],
#                       'str_values': ['abc', 'def', 'ghi']})
#
#
# r_dataframe = pandas2ri.py2rpy(pd_df)
# print(r_dataframe)

import rpy2.robjects as robjects
from rpy2.robjects import pandas2ri
from rpy2.robjects.packages import importr, data
robjects.r['options'](warn=-1)  # turn warning messages off

pandas2ri.activate()   # very import step !!!!!


# read in core functions
lme4 =     importr('lme4')
lmerTest = importr('lmerTest')
emmeans =  importr('emmeans')
base = importr('base')


r_dataframe = pandas2ri.py2rpy(mydf)
print(r_dataframe)

print(mydf.columns.values)
print(mydf.Sample_Date.unique())

res = lme4.lmer('sodium ~ treatment + (1 + treatment|ID)', data = r_dataframe)

#print(res)

# this will run straight R code in R land
# robjects.r('''
# library(lme4)
# library(lmerTest)
# data(dietox, package='geepack')
# m<-lmer('Weight ~ Time + (1+Time|Pig)', data=dietox)
# print(summary(m))
# ''')



exit()





# base.print(pi)
#
# dietox = data(geepack).fetch('dietox')['dietox']
# base.print(dietox)
# r.top(dietox)
#
# exit()

# from rpy2.robjects.vectors import StrVector
#
#

#
#
# dietox = data(geepack).fetch('dietox')['dietox']
#
# rpy2.robjects.r['dietox']
#
