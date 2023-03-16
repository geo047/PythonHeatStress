import matplotlib.pyplot as plt
import matplotlib
import pandas as pd
import numpy as np
import myplots as myplt
from createInputFile import read_clean


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
fig.subplots_adjust(hspace=0.6, wspace=0.6)
counter = 0
for ii in cols[0:9]:
    counter += 1
    ax = fig.add_subplot(3, 3, counter)

    # plottype is for which axis is to remain on
    lookup = pd.DataFrame({'counter':np.arange(0,9,1),
                           'plottype':['y','none','none',
                                       'y','none','none',
                                       'xy','xy','xy' ]})
    x = lookup.loc[lookup['counter'] == counter-1, 'plottype' ].item()
    p = myplt.my_plot(df=mydf, traitnme=ii, plottype = x )
plt.savefig('multiplotfig1.jpg', dpi=300)


fig = plt.figure()
fig.subplots_adjust(hspace=0.6, wspace=0.6)
counter = 0
for ii in cols[0:9]:
    counter += 1
    ax = fig.add_subplot(3, 3, counter)

    # plottype is for which axis is to remain on
    lookup = pd.DataFrame({'counter':np.arange(0,9,1),
                           'plottype':['y','none','none',
                                       'y','none','none',
                                       'xy','xy','xy' ]})
    x = lookup.loc[lookup['counter'] == counter-1, 'plottype' ].item()
    p = myplt.my_plot(df=mydf, traitnme=ii, plottype = x )
plt.savefig('multiplotfig1.jpg', dpi=300)



fig = plt.figure()
fig.subplots_adjust(hspace=0.6, wspace=0.6)
counter = 0
for ii in cols[9:18]:
    counter += 1
    ax = fig.add_subplot(3, 3, counter)

    # plottype is for which axis is to remain on
    lookup = pd.DataFrame({'counter':np.arange(0,9,1),
                           'plottype':['y','none','none',
                                       'y','none','none',
                                       'xy','xy','xy' ]})
    x = lookup.loc[lookup['counter'] == counter-1, 'plottype' ].item()
    p = myplt.my_plot(df=mydf, traitnme=ii, plottype = x )
plt.savefig('multiplotfig2.jpg', dpi=300)



fig = plt.figure()
fig.subplots_adjust(hspace=0.6, wspace=0.6)
counter = 0
for ii in cols[18:27]:
    counter += 1
    ax = fig.add_subplot(3, 3, counter)

    # plottype is for which axis is to remain on
    lookup = pd.DataFrame({'counter':np.arange(0,9,1),
                           'plottype':['y','none','none',
                                       'y','none','none',
                                       'xy','xy','xy' ]})
    x = lookup.loc[lookup['counter'] == counter-1, 'plottype' ].item()
    p = myplt.my_plot(df=mydf, traitnme=ii, plottype = x )
plt.savefig('multiplotfig3.jpg', dpi=300)




fig = plt.figure()
fig.subplots_adjust(hspace=0.6, wspace=0.6)
counter = 0
for ii in cols[27:32]:
    counter += 1
    ax = fig.add_subplot(3, 3, counter)

    # plottype is for which axis is to remain on
    lookup = pd.DataFrame({'counter':np.arange(0,9,1),
                           'plottype':['y','none','none',
                                       'y','none','none',
                                       'xy','xy','xy' ]})
    x = lookup.loc[lookup['counter'] == counter-1, 'plottype' ].item()
    p = myplt.my_plot(df=mydf, traitnme=ii, plottype = x )
plt.savefig('multiplotfig4.jpg', dpi=300)





