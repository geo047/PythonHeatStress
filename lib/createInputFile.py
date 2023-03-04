# Read in raw data, modify, transform,
# and output

import pandas as pd
import numpy as np


def read_clean():

    # Read data sheets
    filenm = "/home/g/PyCharm/PythonHeatStress/Data/acidbu22.xlsx"
    mydf = pd.read_excel(filenm, sheet_name='Sheet1',
                          na_values=".")
    mydf.columns = mydf.columns.str.strip() # remove pesky spaces in col names

    mydf.rename(columns = {'treatment':'Diet'}, inplace=True)
    mydf.sort_values(by=['ID', 'Sample_Date', 'Diet'], inplace=True)
    mydf = mydf.astype( {'ID':'string', 'Sample':'int', 'Diet':'string'}  )
    mydf['Diet'].replace({'trt_1':'Diet I', 'trt_2':'Diet II','trt_3':'Diet III'}, inplace=True)
    # remove rows with these dates 2022-09-22, and after 17/10
    mydf.query('~(Sample_Date=="2022-09-22" or Sample_Date > "2022-10-17") ', inplace=True)
    mydf.Sample -= 1 # reindexing Sample day number to start from 1.


    # create Event column
    conditions = [
        mydf.Sample_Date <= '2022-10-01',
        (mydf.Sample_Date > '2022-10-01') & (mydf.Sample_Date <= '2022-10-08'),
        mydf.Sample_Date > '2022-10-08'
    ]

    values = ['PreHeat', 'Heat', 'Recovery']
    mydf['Event'] = np.select(conditions, values, default=None)
    #print(mydf.groupby('Event').count()) #  the numbers check out.

#    mydf.to_csv('/home/g/PyCharm/PythonHeatStress/Data/cleanedData.csv', index=False)
    mydf.columns = mydf.columns.str.replace(' ', '')
    mydf.columns = mydf.columns.str.replace(':', '_')
    mydf.columns = mydf.columns.str.replace('-', '_')

    # Decided to standardize colums for easier comparison later on
    # Standardizing columns
    print(mydf.head())
    exit()


    normalized_mydf = (mydf - mydf.mean()) / mydf.std()
    print(normalized_mydf.head())
    exit()






    return mydf

def read_add_covariates(df, trait):
    # add time points 1 and 2 as covariates to trait of interest
    time1df = df.query('Sample_Date=="2022-09-27"')[['ID',trait]]
    time1df.rename(columns = {trait:'timecov1'}, inplace=True)
    df = pd.merge(df,time1df, how="left", on="ID")

    time2df = df.query('Sample_Date=="2022-10-01"')[['ID',trait]]
    time2df.rename(columns = {trait:'timecov2'}, inplace=True)
    df = pd.merge(df,time2df, how="left", on="ID")

    return df


def make_2_events(df):
    # removing Sample Time points 1 and 2 from dataframe
    df = df.query('~(Sample == 1 | Sample == 2)')
    return df

