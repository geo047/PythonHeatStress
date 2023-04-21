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
'GammaGT', 'B_hydroxybutyrate' ,'GLDH', 'pH' ,'pCO2' ,'pO2' ,'BE' ,'HCO3',
'LBP', 'LBPlog10', 'SAA', 'SAAlog10']





#-------------------------------------------#
# Create  Plots over Time               #
# Figure 1 in report + individualots for Gene
#-------------------------------------------#
#import createMeanPlots
#import createIndivMeanPlots
#exit()



##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
## One Way Anova of all traits
##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#import oneWayANOVA
# exit()




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

from myfunctions import my_analysis, my_analysisII, my_analysisIII, my_pval, my_convert


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~``
#  Model Building
# Table 1 AIC results in report
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
# for ii, word in enumerate(cols):
#     print(f' TRAIT VALUE = {word}')
#     my_analysis(TRAITvalue=word)
#
# exit()

#----------------------------------------
# Getting p-values for Model II
# Needed for Table 3 of report
#------------------------------------

df_pval = pd.DataFrame(columns=['trait', 'Event', 'DietLevel', 'estimate', 'SE', 't.ratio', 'p.value'])
for ii, word in enumerate(cols):
    print(f' TRAIT VALUE = {word}')
    tempdf = my_pval(TRAITvalue=word)
    df_pval = pd.concat([df_pval, tempdf], axis=0) # row concat
filenm = "/home/g/PyCharm/PythonHeatStress/df_pval.csv"
df_pval.to_csv(filenm, index=False)
print(df_pval)
exit()




#
# # Calculating contrasts of Diet I verse Diet II and III
# # Tables 2A, 2B, and 2C in report
# df_contrasts = pd.DataFrame(columns=['trait', 'Event', 'contrast', 'estimate', 'SE', 't.ratio', 'p.value'])
# for ii in cols:
#     print(f'Trait Value is .... {ii}')
#     tempdf = my_analysisII(TRAITvalue=ii)
#     df_contrasts = pd.concat([df_contrasts, tempdf], axis=0) # row concat
#
#
# # Separate into 3 data files - preHeat, Heat, and Recovery
# df_preHeat = df_contrasts.query('Event == "preHeat"')
# df_Heat = df_contrasts.query('Event == "Heat"')
# df_Recovery = df_contrasts.query('Event == "Recovery"')
#
#
#
# df_preHeat = my_convert(df=df_preHeat)
# df_preHeat  = df_preHeat.replace({'D2 - D1': 'II - I', 'D3 - D1': 'III - I'}, regex= True)
# df_preHeat = df_preHeat.drop(columns = 'Event')
# df_preHeat = df_preHeat.round(3)
# filenm = "/home/g/PyCharm/PythonHeatStress/df_contrasts_preHeat.csv"
# df_preHeat.to_csv(filenm, index=False)
#
#
# df_Heat = my_convert(df=df_Heat)
# df_Heat  = df_Heat.replace({'D2 - D1': 'II - I', 'D3 - D1': 'III - I'}, regex= True)
# df_Heat = df_Heat.drop(columns = 'Event')
# df_Heat = df_Heat.round(3)
# filenm = "/home/g/PyCharm/PythonHeatStress/df_contrasts_Heat.csv"
# df_Heat.to_csv(filenm, index=False)
#
#
#
# df_Recovery = my_convert(df=df_Recovery)
# df_Recovery  = df_Recovery.replace({'D2 - D1': 'II - I', 'D3 - D1': 'III - I'}, regex= True)
# df_Recovery = df_Recovery.drop(columns = 'Event')
# df_Recovery = df_Recovery.round(3)
# filenm = "/home/g/PyCharm/PythonHeatStress/df_contrasts_Recovery.csv"
# df_Recovery.to_csv(filenm, index=False)
#
# # exit()

#--------------------------------------------------------------
# Decided to investigate change in p-values, across traits,
#  via box plots
# Figure 2 in report
# -----------------------------------------------------------------
#
# myplots.my_boxplot(df=df_contrasts)
# exit()
#

#----------------------------------------------
# Adding individual plots as an appendix to report
#----------------------------------------------------------
#
# gg = myplots.my_individual_plot(df=mydf)
# print(gg)
#
# exit()



### Decide not to do the analyses as contrasts as too difficult to interpret the
### contrasts. Sticking to straight estimates (see below)
# df_em = pd.DataFrame(columns=['contrast','estimate','trait'])
# for ii in cols:
#     #    print(f'TRAIT VALUE IS ... {ii}  ..... ')
#
#     tempdf = my_analysisII(TRAITvalue=ii )
#     df_em = pd.concat([df_em, tempdf], axis=0) # row concat
#
# min_neg = df_em.estimate.min()
# max_pos = df_em.estimate.max()
#
# fig = plt.figure()
# counter = 1
# for ii in cols[0:16]:
#     print(f'TRAIT VALUE IS ... {ii}  ..... ')
#
#     dftrait = df_em[df_em.trait == ii]
#     ax = fig.add_subplot(4,4, counter)
#     myplots.rect_plot(fig, ax, dftrait, min_neg, max_pos)
#     counter += 1
#
# filenm = "/home/g/PyCharm/PythonHeatStress/fig1.pdf"
# plt.savefig(filenm)
# #plt.show()
#
# fig = plt.figure()
# counter = 1
# for ii in cols[16:]:
#     print(f'TRAIT VALUE IS ... {ii}  ..... ')
#
#     dftrait = df_em[df_em.trait == ii]
#     ax = fig.add_subplot(4,4, counter)
#     myplots.rect_plot(fig, ax, dftrait, min_neg, max_pos)
#     counter += 1
#
# filenm = "/home/g/PyCharm/PythonHeatStress/fig2.pdf"
# plt.savefig(filenm)
#

#----------------------------------------------------------------------------------------
# 08/03/2023
# Decided to try bar plots instead and dealing with estimates of Diets directly instead
# of contrasts.
#------------------------------------------------------------------------------------------

df_em = pd.DataFrame(columns=['Diet','Event', 'emmean','SE', 'lower.CL', 'upper.CL', 'trait'])
for ii in cols:
    #    print(f'TRAIT VALUE IS ... {ii}  ..... ')
    #  print out estimates instead of contrasts but similar to analysis above.
    tempdf = my_analysisIII(TRAITvalue=ii )
    tempdf['trait'] = ii

    df_em = pd.concat([df_em, tempdf], axis=0) # row concat

myplots.my_bar_plot(df=df_em, eventType="Event2")
myplots.my_bar_plot(df=df_em, eventType="Event3")


df_em = df_em.iloc[:, [ 6, 1, 0, 2, 3, 4, 5 ]]  # reorganize cols to be trait first
df_em = df_em.round(3)  # rount to 3 decimal places

# Convert categorical variable to a string and replace
# duplicate with string value
# Has to be done in this order. Event first, then trait  for
# duplicate removal.
x =  df_em.loc[:,['trait','Event']].duplicated()
df_em.Event = df_em.Event.astype(str)
df_em.loc[x, 'Event'] = ""

x =  df_em.trait.duplicated()
df_em['trait'] = df_em.trait.astype(str)
df_em.loc[x, 'trait']  = ""

# Convert Event and Diet labels into  beter labels for report
df_em['Event'] = df_em['Event'].replace({'Event2':'Heat',
                        'Event3':'Recovery'})
df_em['Diet'] = df_em['Diet'].replace({'Diet I': 'I',
                               'Diet II': 'II',
                               'Diet III':'III'})

print(df_em.head())

filenm = "/home/g/PyCharm/PythonHeatStress/df_em.csv"
df_em.to_csv(filenm, index=False)
print(df_em)

