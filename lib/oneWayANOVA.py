import scipy.stats as stats
import pandas as pd
import numpy as np
from createInputFile import read_clean

mydf = read_clean()

# # obtained by first running createInputFile.py
# mydf = pd.read_csv('/home/g/PyCharm/PythonHeatStress/Data/cleanedData.csv')
# mydf = mydf.astype( {'ID':'string', 'Sample':'int', 'Diet':'string'}  )

# extracting names of the traits in mydf. Removing the fixed effects cols.
cols = mydf.columns.values
cols= np.delete( cols, [0,1,2,3,len(cols)-2, len(cols)-1] )  # trait names from columns of dataframe


print(mydf.Diet.unique())
for ii in cols:
    #print(mydf.query('Diet == "diet I"'))

    fvalue, pvalue = stats.f_oneway(mydf.query('Diet == "Diet I"')[ii],
                                    mydf.query('Diet == "Diet II"')[ii],
                                    mydf.query('Diet == "Diet III"')[ii],
                                    )
    print(f'Trait = {ii }   F value = {round(fvalue,3)} p-value = {round(pvalue,3)}')


