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



def my_individual_plot(df, traitnme:str):
    g = sns.FacetGrid(df, row="treatment", col="Event", margin_titles=True)
    g.map(sns.regplot, "Sample", "sodium", color=".3", fit_reg=False, x_jitter=.1)

    plt.show()
    exit()











    sns.set(font_scale=0.5)
    sns.set_style('ticks')
    #sns.set_palette("bright")

    fig = plt.figure()
    fig.subplots_adjust(hspace=0.4, wspace=0.4)

    # PreHeat   + Diet I
    ax = fig.add_subplot(3, 3, 1)
    dfsub = df.query('Event == "PreHeat"  & treatment == "diet I" ')
    mypal = sns.color_palette("bright", 4, desat=1)
    sp = sns.lineplot(data=dfsub, x='Sample', y=traitnme, hue='ID', sharex=True,
                      alpha=0.925, palette=mypal, lw=2, marker="o")
    sp.set_ylim(df[traitnme].min(), df[traitnme].max())

    sp.grid(False)
    sp.get_legend().remove()



    # Heat   + Diet I
    ax = fig.add_subplot(3, 3, 2)
    dfsub = df.query('Event == "Heat"  & treatment == "diet I" ')
    mypal = sns.color_palette("bright", 4, desat=1)
    sp = sns.lineplot(data=dfsub, x='Sample', y=traitnme, hue='ID', sharex=True,
                      alpha=0.925, palette=mypal, lw=2, marker="o")
    sp.set_ylim(df[traitnme].min(), df[traitnme].max())

    sp.grid(False)
    sp.get_legend().remove()

    # Recovery   + Diet I
    ax = fig.add_subplot(3, 3, 3)
    print(df.Event.unique())

    dfsub = df.query('Event == "Recovery"  & treatment == "diet I" ')
    mypal = sns.color_palette("bright", 4, desat=1)
    sp = sns.lineplot(data=dfsub, x='Sample', y=traitnme, hue='ID', sharex=True,
                      alpha=0.925, palette=mypal, lw=2, marker="o")
    sp.set_ylim(df[traitnme].min(), df[traitnme].max())

    sp.grid(False)
    sp.get_legend().remove()

  #  fig, ax = plt.subplots(nrows=3, ncols=3, sharex=True, sharey=True, figsize=(6, 6))

  #  fig.text(0.5, 0.04, 'common X', ha='center')
  #  fig.text(0.04, 0.5, 'common Y', va='center', rotation='vertical')

    plt.show()
    exit()






#
# mydfplt = mydf.pivot(index='Sample', columns='ID', values='sodium')
# mydfplt.sort_values(by='Sample', inplace=True)
#
# print(mydfplt.head(5))
#
# mydfplt.plot(kind="line")
# plt.show()

