import rpy2.robjects as robjects
from rpy2.robjects import pandas2ri
from rpy2.robjects.packages import importr, data
from createInputFile import read_clean, read_add_covariates
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

TRAITvalue = "sodium"
mydf = read_clean()


r_dataframe = pandas2ri.py2rpy(mydf)  # convert pandas into R dataframe



#-----------------------------------------------
#  Analysis of Sodium Trait
#  No signif interaction or main effects
#  Conclusions:
#   Heat event is having no effect on sodium
#   Diet is having no effect on sodium
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# Full model: random effect allows baseline for animal to change with Event
#m_I_E = lme4.lmer(  TRAITvalue + '~ 1 + Diet*Event +  (1+Event|ID)', data= r_dataframe)

robjects.globalenv["my_r_df"] = r_dataframe
robjects.r('''
library(lme4)
library(emmeans)
heatlme  = lmer('sodium  ~ 1 + Diet*Event + (1+Event|ID)', data = my_r_df )
emm1 = emmeans(heatlme, ~Diet|Event)
print(pairs(emm1))
''')




#
# # Step 1: Testing stat significance of fixed interaction term
# m_I_E = lme4.lmer( TRAITvalue + ' ~ 1 + Diet*Event +  (1+Event|ID)', REML= False, data = r_dataframe)
# m_noI_E = lme4.lmer( TRAITvalue +  ' ~ 1 + Diet + Event + (1+Event|ID)', REML=False, data = r_dataframe)
# print(pb.KRmodcomp(m_I_E, m_noI_E))
# print(stats.drop1(m_I_E, test="Chisq"))
# # both F test and LRT say that fixed interaction term can be dropped
# # from the model
#
#
# # Step 2: Testing significance of main fixed effects
# print(lmerTest.anova_lmerModLmerTest(m_noI_E))
# print(stats.drop1(m_noI_E, test="Chisq"))  # => LRT - no signif main effects
#
