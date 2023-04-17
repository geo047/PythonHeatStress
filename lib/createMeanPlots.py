# Figure 1 in report

import matplotlib.pyplot as plt

import matplotlib
matplotlib.rcParams['figure.figsize'] = [15, 20] # for square canvas

import pandas as pd
import numpy as np
import myplots as myplt
from createInputFile import read_clean

spval = 0.6

mydf = read_clean()

# # obtained by first running createInputFile.py
# mydf = pd.read_csv('/home/g/PyCharm/PythonHeatStress/Data/cleanedData.csv')
# mydf = mydf.astype( {'ID':'string', 'Sample':'int', 'Diet':'string'}  )
# extracting names of the traits in mydf. Removing the fixed effects cols.
cols = mydf.columns.values
cols= np.delete( cols, [0,1,2,3,(len(cols)-2),(len(cols)-1) ] )  # trait names from columns of dataframe



# This is clunky but for some reason, the first time plt.figure is called,
# the first plot in the panel has incorrect font size (they are huge).
# All the multi-panel plots followingn this are fine. Weird.
fig = plt.figure()
####!!!! fig.subplots_adjust(hspace=spval, wspace=spval)
counter = 0
for ii in cols[0:12]:
    counter += 1
    ax = fig.add_subplot(4, 3, counter)

    # plottype is for which axis is to remain on
    lookup = pd.DataFrame({'counter':np.arange(0,12,1),
                           'plottype':['y','none','none',
                                       'y','none','none',
                                       'y','none','none',
                                       'xy','xy','xy' ]})
    x = lookup.loc[lookup['counter'] == counter-1, 'plottype' ].item()
    p = myplt.my_plot(df=mydf, traitnme=ii, plottype = x )


plt.savefig('multiplotfig1.jpg', dpi=300)





fig = plt.figure()
####!!!!! fig.subplots_adjust(hspace= spval, wspace=spval)
counter = 0
for ii in cols[0:12]:
    counter += 1
    ax = fig.add_subplot(4, 3, counter)

    # plottype is for which axis is to remain on
    lookup = pd.DataFrame({'counter':np.arange(0,12,1),
                           'plottype':['y','none','none',
                                       'y','none','none',
                                       'y','none','none',
                                       'xy','xy','xy' ]})
    x = lookup.loc[lookup['counter'] == counter-1, 'plottype' ].item()
    p = myplt.my_plot(df=mydf, traitnme=ii, plottype = x )



plt.savefig('multiplotfig1.jpg', dpi=300)




fig = plt.figure()
fig.subplots_adjust(hspace=spval, wspace=spval)
counter = 0
for ii in cols[12:24]:
    counter += 1
    ax = fig.add_subplot(4, 3, counter)

    # plottype is for which axis is to remain on
    lookup = pd.DataFrame({'counter':np.arange(0,12,1),
                           'plottype':['y','none','none',
                                       'y','none','none',
                                       'y','none','none',
                                       'xy','xy','xy' ]})
    x = lookup.loc[lookup['counter'] == counter-1, 'plottype' ].item()
    p = myplt.my_plot(df=mydf, traitnme=ii, plottype = x )
plt.savefig('multiplotfig2.jpg', dpi=300)



fig = plt.figure()
fig.subplots_adjust(hspace=spval, wspace=spval)
counter = 0
for ii in cols[24:34]:
    counter += 1
    ax = fig.add_subplot(4, 3, counter)

    # plottype is for which axis is to remain on
    lookup = pd.DataFrame({'counter':np.arange(0,12,1),
                           'plottype':['y','none','none',
                                       'y','none','none',
                                       'y','none','none',
                                       'xy','xy','xy' ]})
    x = lookup.loc[lookup['counter'] == counter-1, 'plottype' ].item()
    p = myplt.my_plot(df=mydf, traitnme=ii, plottype = x )
plt.savefig('multiplotfig3.jpg', dpi=300)




