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
from createInputFile import mydf

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
nlme = importr('nlme')
pb = importr('pbkrtest')
printr = robjects.r('print')


r_dataframe = pandas2ri.py2rpy(mydf)  # convert pandas into R dataframe
#
# # baseline model
# # Here, baseline animal value is allowed to be different in
# # the different Events. Not sure if this is better than just having
# # (1|ID) where there is an overall baseline value throughout the study.
# # (1:ID:Event) captures idea that some animals will do inherently better during heat event.
# baseline = lme4.lmer('sodium ~ 1 + (Event|ID)', data= r_dataframe)
# #robjects.r('print(model.comparison)')
# #exit()
#
# ##### print(nlme.ranef(baseline))   # random effect values
# ##### print(flexplot.icc(baseline))
# # ICC = 0.43
# # 43% of the variability  can be explained by clustering of ID within Events
#
# #print(flexplot.visualize(baseline, plot="model"))
# import time
# #time.sleep(10)
#
#
# # Testing: does a more sophisticated random effect for ID do a
# # significantly better job of fitting the data.
# mod1 = lme4.lmer('sodium ~ Diet * Event + (Event|ID) ', data =r_dataframe )
# mod2 = lme4.lmer('sodium ~ Diet * Event + (1|ID) ', data =r_dataframe )
# print(stats.anova(mod2, mod1))
#
# print(lmerTest.anova(mod1))
# exit()
#
# robjects.globalenv["df"] = r_dataframe
#
# robjects.r('''
# library(flexplot)
# library(lme4)
# modfull = lmer('sodium ~ Diet + Event + (Event|ID)' , data =df)
# modreduced = lmer('sodium ~ Diet + Event + (1|ID)', data = df )
# #print(summary(mod1))
# xx = anova(modreduced, modfull)
# print(xx)
# '''
# )
# exit()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#  Model Building and Significance Testing via
#  https://www.ssc.wisc.edu/sscc/pubs/MM/MM_TestEffects.html
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Full model. (Event|ID) is random effect that allows baseline animal effect to
# vary with Event type ie. different animal baseline for each heat event.
# We could also consider (1|ID) which is a random intercept effect that fits an random
# effect for the animal over the entire study.
#  Analysis Steps
#  Test for best random effect (Event|ID) or (1|ID) via AIC
#
#  Test if interaction term Event*Diet is significant via AIC and F value
#
#  If no interaction, test significance of main effects


#-----------------------------------------------
#  Analysis of Sodium Trait
#  Conclusion: Diet is having no impact on sodium
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~




TRAITvalue = "sodium"

# Step 1: Testing if (Event|ID) or (1|ID) is better model
m_I_E = lme4.lmer(  TRAITvalue + '~ 1 + Diet*Event +  (Event|ID)', data= r_dataframe)
m_I_1 = lme4.lmer(TRAITvalue + '~ 1 + Diet*Event +  (1|ID)', data= r_dataframe)
print(stats.anova(m_I_1, m_I_E))


# => modelFull has lower AIC so better model. Use (Event|ID)
# => Difference in AIC's is ~5 so significantly better.

# Step 2: Testing stat significance of fixed interaction term
m_I_E = lme4.lmer( TRAITvalue + ' ~ 1 + Diet*Event +  (Event|ID)', REML= False, data = r_dataframe)
m_noI_E = lme4.lmer( TRAITvalue +  ' ~ 1 + Diet + Event + (Event|ID)', REML=False, data = r_dataframe)
print(pb.KRmodcomp(m_I_E, m_noI_E))
# => p.value = 0.7288 Removing interaction makes no difference.
# Stick with main effects model
print(stats.anova(m_noI_E, m_I_E))
# modelNoInt also has loweer AIC and BIC, confirming better fit to data without  interaction

# Step 3: Testing significance of main fixed effects
print(lmerTest.anova_lmerModLmerTest(m_noI_E))
# => Main effects are not significantly different to 0.

print(stats.drop1(m_noI_E, test="Chisq"))
# => Diet is not having an effect on the model.
# =>   There is a drop in AIC  by removing it (model gets better)
#        and its LRT of full to drop1(Diet) is 0.32 with p-value 0.8256




#-----------------------------------------------
#  Analysis of potassium Trait
#  Conclusion: Diet is having no impact on sodium
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

TRAITvalue = "potassium"

# Step 1: Testing if (Event|ID) or (1|ID) is better model
m_I_E = lme4.lmer(  TRAITvalue + '~ 1 + Diet*Event +  (Event|ID)', data= r_dataframe)
m_I_1 = lme4.lmer(TRAITvalue + '~ 1 + Diet*Event +  (1|ID)', data= r_dataframe)
print(stats.anova(m_I_1, m_I_E))
# => m_I_1 much better model based on lower AIC


# Step 2: Testing stat significance of fixed interaction term
m_I_1 = lme4.lmer( TRAITvalue + ' ~ 1 + Diet*Event +  (1|ID)', REML= False, data = r_dataframe)
m_noI_1 = lme4.lmer( TRAITvalue +  ' ~ 1 + Diet + Event + (1|ID)', REML=False, data = r_dataframe)
print(pb.KRmodcomp(m_I_1, m_noI_1))
print(stats.drop1(m_I_1, test="Chisq"))
#print(stats.confint(m_I_1))

# => Ftest for interaction term is p-value of 0.107.  Non-significance.
# => very slight improvement in  AIC by removing interaction main effect.
# => LRT have p value of 0.094
# Further confirmed by looking at confidence intervals for interaction effects. All intervals include 0.
#robjects.globalenv["mymod"] = m_I_1
#robjects.r('''
#library(lme4)
#print(confint(mymod))
#''')
#exit()


### !!!!!! THIS needs further testing ... not sure if Diet is sign. Do other tests.

# Step 3: Testing significance of main fixed effects
print(lmerTest.anova_lmerModLmerTest(m_noI_1))
# => Diet pval 0.051,  Event pval 0.00386
print(stats.drop1(m_noI_1, test="Chisq"))
# => Diet and Event both significant here.
# Further confirmation - bootstrap
m_noI_1 = lme4.lmer( TRAITvalue +  ' ~ 1 + Diet + Event + (1|ID)', REML=False, data = r_dataframe)
m_noInoD_1 = lme4.lmer( TRAITvalue +  ' ~ 1 + Event + (1|ID)', REML=False, data = r_dataframe)
#### print(pb.PBmodcomp(m_noI_1, m_noInoD_1, nsim=50000,seed=31221743))
# => Dropping Diet is significant. It should be kept in the model

# Step 4: Calculation of contrasts.

diet_emm = emmeans.emmeans(m_noI_1, "Diet")
print(diet_emm)  # confidence intervals
print(emmeans.contrast(diet_emm, 'tukey'))

# contrast              estimate   SE   df t.ratio   p.value
# Diet I  - Diet  II    -0.1201 0.0826 16.1  -1.455  0.3379
# Diet I  - Diet III    -0.1972 0.0826 16.1  -2.388  0.0718
# Diet II - Diet III    -0.0771 0.0813 15.5  -0.948  0.6193




#-----------------------------------------------
#  Analysis of chloride Trait
#  Conclusion: Diet is having no impact on sodium
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

TRAITvalue = "chloride"

# Step 1: Testing if (Event|ID) or (1|ID) is better model
m_I_E = lme4.lmer(  TRAITvalue + '~ 1 + Diet*Event +  (Event|ID)', data= r_dataframe)
m_I_1 = lme4.lmer(TRAITvalue + '~ 1 + Diet*Event +  (1|ID)', data= r_dataframe)
print(stats.anova(m_I_1, m_I_E))
# => m_I_1 better model based on lower AIC



# Step 2: Testing stat significance of fixed interaction term
m_I_1 = lme4.lmer( TRAITvalue + ' ~ 1 + Diet*Event +  (1|ID)', REML= False, data = r_dataframe)
m_noI_1 = lme4.lmer( TRAITvalue +  ' ~ 1 + Diet + Event + (1|ID)', REML=False, data = r_dataframe)
print(pb.KRmodcomp(m_I_1, m_noI_1))
print(stats.drop1(m_I_1, test="Chisq"))
#print(stats.confint(m_I_1))

# => Ftest for interaction term is p-value of 0.85.  Non-significance.
# =>  improvement in  AIC by removing interaction main effect.
# => LRT have p value of 0.8593
# Further confirmed by looking at confidence intervals for interaction effects. All intervals include 0.
robjects.globalenv["mymod"] = m_I_1
robjects.r('''
library(lme4)
print(confint(mymod))
''')




# Step 3: Testing significance of main fixed effects
# Event high signif, Diet insignif
print(lmerTest.anova_lmerModLmerTest(m_noI_1))
# => Diet pval 0.3051,  Event pval 0.000000235

print(stats.drop1(m_noI_1, test="Chisq"))
# => LRT: non-signif for Diet, highly signif for Event


# Further confirmation - bootstrap
m_noI_1 = lme4.lmer( TRAITvalue +  ' ~ 1 + Diet + Event + (1|ID)', REML=False, data = r_dataframe)
m_noInoD_1 = lme4.lmer( TRAITvalue +  ' ~ 1 + Event + (1|ID)', REML=False, data = r_dataframe)
#### print(pb.PBmodcomp(m_noI_1, m_noInoD_1, nsim=1000,seed=31221743))
# => Dropping Diet is NOT significant. It can be dropped from the model


# Step 4: Calculation of contrasts.

diet_emm = emmeans.emmeans(m_noI_1, "Diet")
print(diet_emm)  # confidence intervals
print(emmeans.contrast(diet_emm, 'tukey'))

# => Nothing doing on with Diet contrasts
# contrast           estimate  SE   df t.ratio p.value
# Diet I - Diet II     -0.972 1.1 16.0  -0.882  0.6591
# Diet I - Diet III     0.549 1.1 16.0   0.498  0.8731
# Diet II - Diet III    1.521 1.1 15.9   1.385  0.3719




#-----------------------------------------------
#  Analysis of bicarbonate Trait
#  Conclusion: Diet is having no impact on sodium
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

TRAITvalue = "bicarbonate"

# Step 1: Testing if (Event|ID) or (1|ID) is better model
m_I_E = lme4.lmer(  TRAITvalue + '~ 1 + Diet*Event +  (Event|ID)', data= r_dataframe)
m_I_1 = lme4.lmer(TRAITvalue + '~ 1 + Diet*Event +  (1|ID)', data= r_dataframe)
print(stats.anova(m_I_1, m_I_E))
# => m_I_E better model based on lower AIC and LRT (pvalue=0.0146)



# Step 2: Testing stat significance of fixed interaction term
m_I_E = lme4.lmer( TRAITvalue + ' ~ 1 + Diet*Event +  (Event|ID)', REML= False, data = r_dataframe)
m_noI_E = lme4.lmer( TRAITvalue +  ' ~ 1 + Diet + Event + (Event|ID)', REML=False, data = r_dataframe)
print(pb.KRmodcomp(m_I_E, m_noI_E))
print(stats.drop1(m_I_E, test="Chisq"))
#print(stats.confint(m_I_1))


# => Ftest for interaction term is p-value of 0.49  Non-significance.
# =>  improvement in  AIC by removing interaction main effect.
# => LRT have p value of 0.35
# Further confirmed by looking at confidence intervals for interaction effects. All intervals include 0.
robjects.globalenv["mymod"] = m_I_E
robjects.r('''
library(lme4)
print(confint(mymod))
''')



# Step 3: Testing significance of main fixed effects
# Both Event and Diet Significant
print(lmerTest.anova_lmerModLmerTest(m_noI_E))
# => Diet pval 0.025,  Event pval 0.0008

print(stats.drop1(m_noI_1, test="Chisq"))
# => Conflicting results:  LRT says diet can be dropped from model pval = 0.305, Event signif



# Further confirmation - bootstrap
m_noI_E = lme4.lmer( TRAITvalue +  ' ~ 1 + Diet + Event + (Event|ID)', REML=False, data = r_dataframe)
m_noInoD_E = lme4.lmer( TRAITvalue +  ' ~ 1 + Event + (Event|ID)', REML=False, data = r_dataframe)
#print(pb.PBmodcomp(m_noI_E, m_noInoD_E, nsim=50000,seed=31221743))
# => Diet is significant. Keep in the model.



# Step 4: Calculation of contrasts.

diet_emm = emmeans.emmeans(m_noI_1, "Diet")
print(diet_emm)  # confidence intervals all overlap
print(emmeans.contrast(diet_emm, 'tukey'))

# contrast           estimate  SE   df t.ratio p.value
# Diet I - Diet II     -0.972 1.1 16.0  -0.882  0.6591
# Diet I - Diet III     0.549 1.1 16.0   0.498  0.8731
# Diet II - Diet III    1.521 1.1 15.9   1.385  0.3719


exit()













# Fit models
mod1 = lme4.lmer('sodium ~ Diet + Event + (1|ID:Event) ', data =r_dataframe )
#print(base.summary(mod1))
print(nlme.ranef(mod1))   # random effect values
#robjects.r('print(ranef)')

mod2 = lme4.lmer('sodium ~ Diet + Event + (Event|ID) ', data =r_dataframe )
#print(base.summary(mod1))
print(nlme.ranef(mod2))   # random effect values
#robjects.r('print(ranef)')



exit()



# Looking at each event in turn.
df = mydf.query('Event == "Heat"')[['Diet','ID','sodium', 'Sample']]
r_dataframe = pandas2ri.py2rpy(df)   # convert pandas to R dataframe
#res = lme4.lmer('sodium ~ Diet + (1 + Diet|ID)', data =r_dataframe )
res = lme4.lmer('sodium ~ Diet + (1|ID)', data =r_dataframe )

robjects.r('print(names)')

print(stats.anova(res))
print(base.summary(res))
#print(lmerTest.anova_lmerModLmerTest(res, ddf="Kenward-Roger"))
print(lmerTest.anova_lmerModLmerTest(res))

exit()

xx=flexplot.estimates(res)
print(xx)

# emmeans
emm = emmeans.emmeans(res, "Diet")
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
# #res = lmer('sodium ~ Diet + (1 + Diet|ID)', data = r_dataframe )
# #summary(res)
# ''')




robjects.r('''
library(lme4)
library(emmeans)
heatlme  = lmer('sodium ~ Diet*Event + (1+Diet|ID)', data = my_r_df )
print(summary(heatlme))
print(class(heatlme))
emm1 = emmeans(heatlme, ~Diet|Event)
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
#res = lmer('sodium ~ Diet + (1 + Diet|ID)', data = r_dataframe )
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
