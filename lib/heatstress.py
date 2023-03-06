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
cols = ['sodium', 'potassium' ,'chloride',
 'bicarbonate' ,'NA_Kratio' ,'aniongap' ,'glucose_serum', 'urea' ,'creatinine',
 'calcium' ,'phospate' ,'CA_Pratio' ,'protein_total' ,'albumin' ,'globulin',
 'A_Gratio' ,'billirubin_total' ,'ALP' ,'AST' ,'CK', 'cholesterol' ,'Magnesium',
 'GammaGT', 'B_hydroxybutyrate' ,'GLDH', 'pH' ,'pCO2' ,'pO2' ,'BE' ,'HCO3']



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



df_em = pd.DataFrame(columns=['contrast','estimate','trait'])



for ii in cols[0:2]:
    print(f'TRAIT VALUE IS ... {ii}  ..... ')

    tempdf = my_analysisII(TRAITvalue=ii )
    df_em = pd.concat([df_em, tempdf], axis=0) # row concat

min_neg = df_em.estimate.min()
max_pos = df_em.estimate.max()


for ii in cols[0:2]:

 dftrait = df_em[df_em.trait == ii]
 print(dftrait)
 myplots.rect_plot(dftrait, min_neg, max_pos)
