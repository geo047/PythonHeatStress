import matplotlib.pyplot as plt
import matplotlib
import pandas as pd
import numpy as np
import myplots as myplt


# obtained by first running createInputFile.py
mydf = pd.read_csv('/home/g/PyCharm/PythonHeatStress/Data/cleanedData.csv')
# extracting names of the traits in mydf. Removing the fixed effects cols.
cols = mydf.columns.values
cols= np.delete( cols, [0,1,2,3,29] )  # trait names from columns of dataframe

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

# Individual trait plots
# Diet Event where each plot is trait value (y) verse Sample (x)

ii = 'sodium'
p = myplt.my_individual_plot(df=mydf, traitnme=ii)
plt.savefig(ii+'.pdf')


