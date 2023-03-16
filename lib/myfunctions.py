
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
#       print(graphics.pairs(em))
#       ct = xx.rx(10)   ## contains p-values
# # Convert R list object into R dataframe and then R dataframe to pandaas dataframe
#       ctnew = base.as_data_frame(ct)  # needed to convert methods.RS4 to R dataframe to convert into pandas dataframe
#       df = pandas2ri.rpy2py_dataframe(ctnew)

#
#  Model Building and Significance Testing via
#  https://www.ssc.wisc.edu/sscc/pubs/MM/MM_TestEffects.html



import numpy as np
import pandas as pd
import rpy2.robjects as robjects
from rpy2.robjects import pandas2ri
from rpy2.robjects.packages import importr, data
from createInputFile import read_clean, read_add_covariates, make_2_events
pandas2ri.activate()   # very import step !!!!!

# read in core functions
lme4 =     importr('lme4')
lmerTest = importr('lmerTest')
emmeans =  importr('emmeans')
graphics = importr('graphics')
base =     importr('base')
stats =    importr('stats')
methods =  importr('methods')
flexplot = importr('flexplot')
nlme =     importr('nlme')
pb =       importr('pbkrtest')
printr =    robjects.r('print')

def my_analysis(TRAITvalue):
    # Model Building

    mydf = read_clean()
    df = read_add_covariates(df=mydf, trait=TRAITvalue)
#    mydf = make_2_events(df=df)
    r_dataframe = pandas2ri.py2rpy(mydf)  # convert pandas into R dataframe
    robjects.globalenv["my_r_df"] = r_dataframe
    robjects.globalenv["tnme"] = TRAITvalue

    frm = stats.as_formula(TRAITvalue + ' ~ 1 + Diet*Event')
    mod1 = stats.lm(frm, data=r_dataframe)
    print(stats.BIC(mod1))

    frm = stats.as_formula(TRAITvalue + ' ~ 1 + Diet*Event + (1|ID)')
    mod2 = lme4.lmer(frm, data=r_dataframe)

    frm = stats.as_formula(TRAITvalue + ' ~ 1 + Diet*Event + (Event|ID)')
    mod3 = lme4.lmer(frm, data=r_dataframe)
    print(stats.anova(mod2, mod3))
 #   print(stats.anova(mod1,mod3))
    print(' ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ')

 #   print(pb.PBmodcomp(mod3, mod2 , nsim=1000, seed=101) )

    return print("Completed ...")

def my_pval(TRAITvalue):
    # Calculating pvalues for levels of Event:Diet in model II

    mydf = read_clean()
    df = read_add_covariates(df=mydf, trait=TRAITvalue)
#    mydf = make_2_events(df=df)
    r_dataframe = pandas2ri.py2rpy(mydf)  # convert pandas into R dataframe
    robjects.globalenv["my_r_df"] = r_dataframe
    robjects.globalenv["tnme"] = TRAITvalue


    frm = stats.as_formula(TRAITvalue + ' ~ 1 + Diet*Event + (1|ID)')
    mod2 = lme4.lmer(frm, data=r_dataframe)
    frm = stats.as_formula(' ~ Event:Diet')
    em = emmeans.emmeans(object=mod2, specs=frm)

    ct = emmeans.contrast(em, adjust="holm")
    ctnew = base.as_data_frame(ct)  # needed to convert methods.RS4 to R dataframe to convert into pandas dataframe
    df = pandas2ri.rpy2py_dataframe(ctnew)
    df = df.round(3)
    df = df.reset_index()  # needed to do this because index started from 1 and would not concat properly.
    traitcol = pd.DataFrame( {'trait': np.repeat(TRAITvalue, df.shape[0])} )
    df = pd.concat([traitcol, df], axis=1)

    df[['Event', 'DietName', 'DietLevel', 'rubbish']] = df['contrast'].str.split(' ', expand=True)
    df.sort_values(['Event', 'DietLevel'], inplace=True)
    df = df[['trait', 'Event', 'DietLevel', 'estimate', 'SE', 't.ratio', 'p.value']]

    # Convert categorical variable to a string and replace
    # duplicate with string value
    # Has to be done in this order. Event first, then trait  for
    # duplicate removal.
    x = df.loc[:, ['trait', 'Event']].duplicated()
    df.Event = df.Event.astype(str)
    df.loc[x, 'Event'] = ""

    x = df.trait.duplicated()

    df['trait'] = df.trait.astype(str)
    df.loc[x, 'trait'] = ""


    # Convert Event labels into  beter labels for report
    df['Event'] = df['Event'].replace({'Event1': 'preHeat',
                                       'Event2': 'Heat',
                                        'Event3': 'Recovery'})



    return df












def my_analysisII(TRAITvalue):
    # Function no longer in use.
    # Original idea was to look at contrasts of diet 1 and 2 against 3 for HEat and REcovery
    # However, contrast differences were too difficult to interpret. Can have a positive difference
    # for a number of different situations.  Rectangular plots not interpretable.

    mydf = read_clean()
    df = read_add_covariates(df=mydf, trait=TRAITvalue)
    mydf = make_2_events(df=df)
    r_dataframe = pandas2ri.py2rpy(mydf)  # convert pandas into R dataframe
    robjects.globalenv["my_r_df"] = r_dataframe
    robjects.globalenv["tnme"] = TRAITvalue
    frm = stats.as_formula(TRAITvalue + ' ~ 1 + timecov1 + timecov2 + Diet*Event + (1|ID)')
    heatlme = lme4.lmer(frm, data=r_dataframe)
    frm = stats.as_formula( ' ~ Diet:Event')
    #    em = emmeans.emmeans(object=heatlme, specs='~ Diet:Event')
    em = emmeans.emmeans(object=heatlme, specs=frm)
    D1H = np.array([1,0,0,0,0,0])
    D2H = np.array([0,1,0,0,0,0])
    D3H = np.array([0,0,1,0,0,0])
    D1R = np.array([0,0,0,1,0,0])
    D2R = np.array([0,0,0,0,1,0])
    D3R = np.array([0,0,0,0,0,1])
    Rvec = np.array([0,0,0,1,1,1])
    Hvec = np.array([1,1,1,0,0,0])
    conlist = robjects.ListVector({
                    "Recovery - Heat" : Rvec - Hvec,
                    "Heat: D1 - D3" : D1H - D3H,
                    "Heat: D2 - D3" : D2H - D3H,
                    "Recovery: D1 - D3" : D1R - D3R,
                    "Recovery: D2 - D3" : D2R - D3R })
    ct = emmeans.contrast(em, method=conlist )  # ct of type methods.RS4
    ctnew = base.as_data_frame(ct) # needed to convert methods.RS4 to R dataframe to convert into pandas dataframe
    fd = pandas2ri.rpy2py_dataframe(ctnew)
    fd = fd.loc[:,('contrast','estimate')]
    fd['trait'] = TRAITvalue
    return fd


def my_analysisIII(TRAITvalue):
    # Analysis similar to my_analysisII except that I am returning estimates of
    # factor levels instead of estimatees of difference in factor levels. More easily
    # intepreted. Plot will be a bar plot.

    # import numpy as np
    # import pandas as pd
    import rpy2.robjects as ro
    # from rpy2.robjects.packages import importr
    # from rpy2.robjects import pandas2ri
    from rpy2.robjects.conversion import localconverter
    #
    # ones_df = np.ones(shape=(48, 614))
    # ones_df = pd.DataFrame(ones_df)
    # with localconverter(ro.default_converter + pandas2ri.converter):
    #     r_from_pd_df = ro.conversion.py2rpy(ones_df)
    # print(type(r_from_pd_df))
    # exit()




    mydf = read_clean()  # create null dataframe
    df = read_add_covariates(df=mydf, trait=TRAITvalue)
    mydf = make_2_events(df=df)  # add events to dataframe

    r_dataframe = pandas2ri.py2rpy(mydf)  # convert pandas into R dataframe

    # store R objects sitting in python in R land
    robjects.globalenv["my_r_df"] = r_dataframe
    robjects.globalenv["tnme"] = TRAITvalue

    # Fit model
    frm = stats.as_formula(TRAITvalue + ' ~ 1 + timecov1 + timecov2 + Diet*Event + (1|ID)')
    heatlme = lme4.lmer(frm, data=r_dataframe)


    # Fit emmeans model
    frm = stats.as_formula(' ~ Diet:Event')
    em = emmeans.emmeans(object=heatlme, specs=frm)
    em = base.as_data_frame(em)  # converting S4 object into R data frame
    with localconverter(ro.default_converter + pandas2ri.converter):
        fd = robjects.conversion.get_conversion().rpy2py(em)  # conver R dataframe to pandas dataframe

    fd = fd.loc[:, ('Diet', 'Event', 'emmean', 'SE', 'lower.CL', 'upper.CL')]
    fd['trait'] = TRAITvalue

    return fd

