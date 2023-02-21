# Plotting functions
import matplotlib.pyplot as plt
import seaborn as sns

def my_plot(df, ylab:str):
    sp = sns.lineplot(df)
    sp.set(xlabel="collection day", ylabel=ylab)
    plt.show()

#
# mydfplt = mydf.pivot(index='Sample', columns='ID', values='sodium')
# mydfplt.sort_values(by='Sample', inplace=True)
#
# print(mydfplt.head(5))
#
# mydfplt.plot(kind="line")
# plt.show()

