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


def my_analysis(TRAITvalue):

    mydf = read_clean()

    r_dataframe = pandas2ri.py2rpy(mydf)  # convert pandas into R dataframe

    robjects.globalenv["my_r_df"] = r_dataframe
    robjects.globalenv["tnme"] = TRAITvalue

    robjects.r('''
    library(lme4)
    library(emmeans)
    frm = as.formula(paste(tnme , ' ~ 1 + Diet*Event + (1+Event|ID)'))
    
    
    heatlme  = lmer(frm, data = my_r_df )

    print(summary(heatlme))
    emm1 = emmeans(heatlme, ~Diet|Event)
    print(pairs(emm1))
    ''')

    return print("Completed ...")

