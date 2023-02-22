# Plotting functions
import matplotlib.pyplot as plt
import seaborn as sns


def my_plot(df, traitnme:str):
    sns.set(font_scale=0.5)
    sns.set_style('ticks')
    #sns.set_palette("bright")

    mypal = sns.color_palette("bright", 3, desat=1)

    # Use palplot and pass in the variable:

    sp = sns.lineplot(data=df, x='Sample', y=traitnme, hue='treatment', errorbar=('se', 1.96),
                      hue_order=['diet I', 'diet II', 'diet III'], alpha=0.925, palette=mypal, lw=3)
    sp.set(xlabel="collection day", ylabel= ('mean within diet')   , title= traitnme )
    sp.grid(False)
    handles, labels = sp.get_legend_handles_labels()
    sp.legend(handles=handles[0:], labels=labels[0:])
    plt.legend(loc='upper right')
    plt.setp(sp.get_legend().get_texts(), fontsize='4')
    plt.axvline(x=2.5, linestyle='dashed')
    plt.axvline(x=7.5, linestyle='dashed')
    return sp
    #plt.show()

#
# mydfplt = mydf.pivot(index='Sample', columns='ID', values='sodium')
# mydfplt.sort_values(by='Sample', inplace=True)
#
# print(mydfplt.head(5))
#
# mydfplt.plot(kind="line")
# plt.show()

