# first draft


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


#-----------------------------------
# Create Input File
#----------------------------------
import createInputFile

# obtained by first running createInputFile.py
mydf = pd.read_csv('/home/g/PyCharm/PythonHeatStress/Data/cleanedData.csv')
# extracting names of the traits in mydf. Removing the fixed effects cols.
cols = mydf.columns.values
cols= np.delete( cols, [0,1,2,3,29] )  # trait names from columns of dataframe



#-------------------------------------------#
# Create  Plots over Time               #
#-------------------------------------------#
import createMeanPlots

exit()





##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
## One Way Anova of all traits
##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import oneWayANOVA


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

pandas2ri.activate()   # very import step !!!!!


# read in core functions
lme4 =     importr('lme4')
lmerTest = importr('lmerTest')
emmeans =  importr('emmeans')
base = importr('base')
stats =  importr('stats')
methods = importr('methods')
flexplot = importr('flexplot')


# Looking at each event in turn.
df = mydf.query('Event == "Heat"')[['treatment','ID','sodium', 'Sample']]
r_dataframe = pandas2ri.py2rpy(df)   # convert pandas to R dataframe
#res = lme4.lmer('sodium ~ treatment + (1 + treatment|ID)', data =r_dataframe )
res = lme4.lmer('sodium ~ treatment + (1|ID)', data =r_dataframe )

robjects.r('print(names)')

print(stats.anova(res))
print(base.summary(res))
#print(lmerTest.anova_lmerModLmerTest(res, ddf="Kenward-Roger"))
print(lmerTest.anova_lmerModLmerTest(res))

exit()

xx=flexplot.estimates(res)
print(xx)

# emmeans
emm = emmeans.emmeans(res, "treatment")
base.print(emm)
#exit()

# for viewing some of the results but still not the best because it is not over Sample
print(base.summary(res))
xx=flexplot.visualize(res, plot="model")
base.print(xx)
import time
#time.sleep(40)









with ro.default_converter + pandas2ri.converter:
  r_from_pd_df = ro.conversion.get_conversion().py2rpy(mydf)
robjects.globalenv["my_r_df"] = r_from_pd_df
robjects.r('print(my_r_df[1:5,])')

# robjects.r('''
# library(lme4)
# print(r_dataframe)
# #res = lmer('sodium ~ treatment + (1 + treatment|ID)', data = r_dataframe )
# #summary(res)
# ''')




robjects.r('''
library(lme4)
library(emmeans)
heatlme  = lmer('sodium ~ treatment*Event + (1+treatment|ID)', data = my_r_df )
print(summary(heatlme))
print(class(heatlme))
emm1 = emmeans(heatlme, ~treatment|Event)
print(pairs(emm1))


''')

print("the end ")

exit()


# TO DO
# 1. create new variable based on data for events Pre, Heat, Recovery
# 2 Run lmer analysis for each event type for each trait

rcode = robjects.r('''
library(lme4)
print(r_dataframe)
#print(df)
#res = lmer('sodium ~ treatment + (1 + treatment|ID)', data = r_dataframe )
#summary(res)
'''
)


exit()


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
