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

TRAITvalue = "bicarbonate"
mydf = read_clean()


r_dataframe = pandas2ri.py2rpy(mydf)  # convert pandas into R dataframe



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

