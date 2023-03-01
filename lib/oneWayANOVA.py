import scipy.stats as stats
import pandas as pd
import numpy as np



# obtained by first running createInputFile.py
mydf = pd.read_csv('/home/g/PyCharm/PythonHeatStress/Data/cleanedData.csv')
# extracting names of the traits in mydf. Removing the fixed effects cols.
cols = mydf.columns.values
cols= np.delete( cols, [0,1,2,3,29] )  # trait names from columns of dataframe




for ii in cols:
    #print(mydf.query('treatment == "diet I"'))

    fvalue, pvalue = stats.f_oneway(mydf.query('treatment == "diet I"')[ii],
                                    mydf.query('treatment == "diet II"')[ii],
                                    mydf.query('treatment == "diet III"')[ii],
                                    )
    print(f'Trait = {ii }   F value = {round(fvalue,3)} p-value = {round(pvalue,3)}')

