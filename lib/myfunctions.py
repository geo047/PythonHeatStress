
# Notes:
# Full model:
# y ~ Diet*Event + (1 + Event|ID)
# random effect of animal is allowed to change within Event type
# Usefull commands
#       print(stats.anova(mod2, mod1))
#       print(lmerTest.anova(mod1))
#       robjects.globalenv["df"] = r_dataframe
#       print(base.summary(mod1))
#       print(nlme.ranef(mod1))   # random effect values
#       robjects.r('print(ranef)')

#
#  Model Building and Significance Testing via
#  https://www.ssc.wisc.edu/sscc/pubs/MM/MM_TestEffects.html




import rpy2.robjects as robjects
from rpy2.robjects import pandas2ri
from rpy2.robjects.packages import importr, data
from createInputFile import read_clean, read_add_covariates, make_2_events
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
    frm = as.formula(paste(tnme , ' ~ 1 + Diet*Event + (1|ID)'))
    
    
    heatlme  = lmer(frm, data = my_r_df )

    #print(summary(heatlme))
    emm1 = emmeans(heatlme, ~Diet|Event)
    print(pairs(emm1))
    ''')

    return print("Completed ...")


def my_analysisII(TRAITvalue):


    mydf = read_clean()
    df = read_add_covariates(df=mydf, trait=TRAITvalue)
    mydf = make_2_events(df=df)



    r_dataframe = pandas2ri.py2rpy(mydf)  # convert pandas into R dataframe

    robjects.globalenv["my_r_df"] = r_dataframe
    robjects.globalenv["tnme"] = TRAITvalue

    robjects.r('''
    library(lme4)
    library(emmeans)
    library(lmerTest)
    frm = as.formula(paste(tnme , ' ~ 1 + timecov1 + timecov2 + Diet*Event + (1|ID)'))




    heatlme  = lmer(frm, data = my_r_df )
    options(width=400)
     em = emmeans(heatlme,   specs = ~ Diet:Event)  
     #print(em)
     D1H = c(1,0,0,0,0,0)
     D2H = c(0,1,0,0,0,0)
     D3H = c(0,0,1,0,0,0)
     D1R = c(0,0,0,1,0,0)
     D2R = c(0,0,0,0,1,0)
     D3R = c(0,0,0,0,0,1)
     R = c(0,0,0,1,1,1)
     H = c(1,1,1,0,0,0)

     ct = contrast(em, 
     # method=list("Heat: D1 - D3"=D1H - D3H,
     #             "Heat: D2 - D3" = D2H - D3H,
     #             "Recovery: D1 - D3"=D1R - D3R,
     #             "Recovery: D2 - D3" = D2R - D3R) )
 
     method=list("Recovery - Heat" = R - H,  
                 "Heat: D1 - D3"=D1H - D3H,
                 "Heat: D2 - D3" = D2H - D3H))
                  "Recovery: D1 - D3"=D1R - D3R,
                 "Recovery: D2 - D3" = D2R - D3R) )

                                    
     print(ct)
 #   emm1 = emmeans(heatlme, ~Diet|Event)
 #    print(pairs(emm1))
#     print(summary(heatlme)["coefficients"])
    
    ''')

    return print("Completed ...")


