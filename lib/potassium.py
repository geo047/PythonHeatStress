import rpy2.robjects as robjects
from rpy2.robjects import pandas2ri
from rpy2.robjects.packages import importr, data
from createInputFile import read_clean
pandas2ri.activate()   # very import step !!!!!

# read in core functions
lme4 =     importr('lme4')
lmerTest = importr('lmerTest')
emmeans =  importr('emmeans')
base =     importr('base')
stats =    importr('stats')
methods =  importr('methods')
flexplot = importr('flexplot')
nlme =     importr('nlme')
pb =       importr('pbkrtest')
printr =    robjects.r('print')


# read dataframe
mydf = read_clean()
r_dataframe = pandas2ri.py2rpy(mydf)  # convert pandas into R dataframe

robjects.globalenv["my_r_df"] = r_dataframe
robjects.r('''
library(lme4)
library(emmeans)
heatlme  = lmer('sodium  ~ 1 + Diet*Event + (1+Event|ID)', data = my_r_df )
emm1 = emmeans(heatlme, ~Diet|Event)
print(pairs(emm1))
''')



#-----------------------------------------------
#  Analysis of potassium Trait
#  Conclusion:
# Hard to tell what is going on here.
# Interaction is non-significant and dropped from model.
# Diet significant and non-signi depending on test.
#     - when significant, it was barely at 5% level.
# But contrasts show signi difference between diet I and III.
# Event is significant. Sign diff of Heat and pre-Heat at 0.04
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#TRAITvalue = "potassium"
#
# m_I_E = lme4.lmer(  TRAITvalue + '~ 1 + Diet*Event +  (1+Event|ID)', data= r_dataframe)
#
# # Step 2: Testing stat significance of fixed interaction term
# m_I_E = lme4.lmer( TRAITvalue + ' ~ 1 + Diet*Event +  (1+Event|ID)', REML= False, data = r_dataframe)
# m_noI_E = lme4.lmer( TRAITvalue +  ' ~ 1 + Diet + Event + (1+Event|ID)', REML=False, data = r_dataframe)
# print(pb.KRmodcomp(m_I_E, m_noI_E))  # inter not signif
# print(stats.drop1(m_I_E, test="Chisq"))  # LRT inter not signific
#
# #robjects.globalenv["mymod"] = m_I_E
# #robjects.r('''
# #library(lme4)
# #print(confint(mymod))
# #''')  # All confidence intervals for inter include 0
# #exit()
#
#
# # Step 2: Testing significance of main fixed effects
# print(lmerTest.anova_lmerModLmerTest(m_noI_E)) # both effects significant
# print(stats.drop1(m_noI_E, test="Chisq"))  # BUT conflicting AIC and LRT conclusions
#
# m = lme4.lmer( TRAITvalue +      ' ~ 1 + Diet + Event  +  (1+Event|ID)', REML= False, data = r_dataframe)
# m_noD = lme4.lmer( TRAITvalue +  ' ~ 1 +        Event  + (1+Event|ID)', REML=False, data = r_dataframe)
# m_noE = lme4.lmer( TRAITvalue +  ' ~ 1 + Diet          + (1+Event|ID)', REML=False, data = r_dataframe)
#
# print(pb.KRmodcomp(m, m_noD))  # Diet significant at p=0.049
# print(pb.KRmodcomp(m, m_noE))  # Event significant at p=0.047
#
# # Further confirmation - bootstrap
# m_noI_E = lme4.lmer( TRAITvalue +  ' ~ 1 + Diet + Event + (1+Event|ID)', REML=False, data = r_dataframe)
# m_noInoD_E = lme4.lmer( TRAITvalue +  ' ~ 1 + Event + (1+Event|ID)', REML=False, data = r_dataframe)
# #print(pb.PBmodcomp(m_noI_E, m_noInoD_E, nsim=5000,seed=31221743))
# # => Bootstrap saying Diet is not significant
#
# m_noI_E = lme4.lmer( TRAITvalue +  ' ~ 1 + Diet + Event + (1+Event|ID)', REML=False, data = r_dataframe)
# m_noInoE_E = lme4.lmer( TRAITvalue +  ' ~ 1 + Diet + (1+Event|ID)', REML=False, data = r_dataframe)
# #print(pb.PBmodcomp(m_noI_E, m_noInoE_E, nsim=5000,seed=31221743))
# # => Bootstrap saying Event is significant
#
# # Step 3: Looking at contrasts. Diet I and III different
# diet_emm = emmeans.emmeans(m_noI_E, "Diet")
# print(diet_emm)  # confidence intervals
# print(emmeans.contrast(diet_emm, 'tukey'))
#
# # contrast           estimate     SE   df t.ratio p.value
# # Diet I - Diet II     -0.121 0.0816 10.9  -1.484  0.3357
# # Diet I - Diet III    -0.228 0.0816 10.9  -2.788  0.0433
# # Diet II - Diet III   -0.106 0.0809 10.6  -1.315  0.4173
#
#
# # Step 3: Looking at contrasts.
# event_emm = emmeans.emmeans(m_noInoD_E, "Event")
# print(event_emm)  # confidence intervals
# print(emmeans.contrast(event_emm, 'tukey'))
#
# # Heat - PreHeat      -0.2358 0.0847 12.5  -2.784  0.0396
# # Heat - Recovery     -0.0525 0.0538 11.2  -0.976  0.6057
# # PreHeat - Recovery   0.1833 0.0890 13.5   2.059  0.1360
#
#
#
