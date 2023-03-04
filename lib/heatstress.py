# first draft

import myplots
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import rpy2.robjects as ro
from rpy2.robjects.packages import importr
from rpy2.robjects import pandas2ri


pd.set_option('display.max_columns', 30)
pd.set_option('display.min_rows', 100)
pd.set_option('display.width', 800)
pd.set_option('display.max_colwidth', 20)
from createInputFile import read_clean


#-----------------------------------
# Read data and create dataframe
#----------------------------------

mydf = read_clean()

#
# # obtained by first running createInputFile.py
# mydf = pd.read_csv('/home/g/PyCharm/PythonHeatStress/Data/cleanedData.csv')
# # extracting names of the traits in mydf. Removing the fixed effects cols.
cols = mydf.columns.values
cols= np.delete( cols, [0,1,2,3,29] )  # trait names from columns of dataframe



#-------------------------------------------#
# Create  Plots over Time               #
#-------------------------------------------#
#import createMeanPlots
#exit()





##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
## One Way Anova of all traits
##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#import oneWayANOVA





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

from myfunctions import my_analysis, my_analysisII

# print(cols)
#
# for ii in cols:
#   print(f'Trait Value is .... {ii}')
#   my_analysis(TRAITvalue=ii)

# => Found that there were no significant contrasts in PreHeat.
# Going to implement Ross's idea.

#myplots.my_individual_plot(df=mydf, traitnme = "Magnesium")
#exit()





for ii in cols:
  print(f'TRAIT VALUE IS ... {ii}  ..... ')
  my_analysisII(TRAITvalue=ii )


