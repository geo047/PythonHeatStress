
import matplotlib.pyplot as plt

import matplotlib
matplotlib.rcParams['figure.figsize'] = [15, 20] # for square canvas

import pandas as pd
import numpy as np
import myplots as myplt
from createInputFile import read_clean

spval = 0.6

mydf = read_clean()
cols = mydf.columns.values
cols= np.delete( cols, [0,1,2,3,(len(cols)-2),(len(cols)-1) ] )  # trait names from columns of dataframe


for ii in cols:
    p = myplt.my_mean_plot(df=mydf, traitnme=ii )
    print("plot being printed ... ")



