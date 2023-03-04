# Plotting functions
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np


def my_plot(df, traitnme:str):
    sns.set(font_scale=0.5)
    sns.set_style('ticks')
    #sns.set_palette("bright")

    mypal = sns.color_palette("bright", 3, desat=1)

    # Use palplot and pass in the variable:

    sp = sns.lineplot(data=df, x='Sample', y=traitnme, hue='Diet', errorbar=('se', 1.96),
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


def my_individual_plot(df, traitnme:str):
    #g = sns.FacetGrid(df, row="Diet", col="Event", margin_titles=True )
    #g.map(sns.regplot, "Sample", "sodium",   hue="ID",  kind="line")

    sns.set_theme(style="ticks")

    palette = sns.color_palette("rocket_r")

    # Plot the lines on two facets
    # sns.relplot(
    #     data=dots,
    #     x="time", y="firing_rate",
    #     hue="coherence", size="choice", col="align",
    #     kind="line", size_order=["T1", "T2"], palette=palette,
    #     height=5, aspect=.75, facet_kws=dict(sharex=False),
    # )

    myid = df['ID'].unique()

    # Used this bit of code to work out what animals belong to Diets
    #tmp = df[['ID', 'Diet']].drop_duplicates(inplace=False)
    #print(tmp.sort_values(['Diet', 'ID']))
    #exit()


    #myid.sort()  # sorts inplace
    myid = ['3795', '3793', '3796',
            '3799', '3794', '3798',
            '3801', '3797', '3803',
            '3802', '3805', '3804'
            ]


    #df = df[['Diet','ID']].drop_duplicates()
    #print(df)

    g = sns.relplot(data=df, x="Sample", y=traitnme, hue="ID",
                    row="Diet", height = 5, aspect=0.75, style="ID", kind="line",
                    row_order=['Diet I', 'Diet II', 'Diet III'], markers="o",
                    linewidth=3,
                    hue_order=myid, palette=sns.color_palette("tab10", 3),
                    facet_kws={"margin_titles": True},
                    dashes = [(1,1),(2,1),(1,1),(1,1),(3,1),(2,1),(2,1),(3,1),(4,1),(3,1),(4,1),(4,1) ]
                    )

    # g = sns.relplot(data=df, x="Sample", y=traitnme, hue="ID", kind="line",
    #                 row="Diet", col="Event", height = 5, aspect=0.75,
    #                 row_order=['Diet I', 'Diet II', 'Diet III'], markers="o",
    #                 col_order=['PreHeat', 'Heat', "Recovery"], linewidth=3,
    #                 hue_order=myid, palette=sns.color_palette("tab10", 3),
    #                 facet_kws={"margin_titles": True}
    #                 )




    lenofarray = len(df['Sample'].unique())
    lenofarray += 1
    g.set(xticks=np.arange(1, lenofarray, 1))
    g.set_xticklabels(np.arange(1, lenofarray, 1) )


#    g.set_titles('{col_name}')
#    [plt.setp(ax.texts, text="") for ax in g.axes.flat]  # remove the original texts
    # important to add this before setting titles
#    g.set_titles(row_template='{row_name}', col_template='{col_name}')

    g.set_titles(col_template="{col_name}", row_template="{row_name}")

    g.set_ylabels(traitnme, clear_inner=False)
    g.set_xlabels("Day Number",  clear_inner=False)
    g.fig.suptitle(traitnme, fontsize=16)
    g.fig.subplots_adjust(top=0.9, bottom=0.1)
    g.legend.remove()
    plt.show()
    exit()











    sns.set(font_scale=0.5)
    sns.set_style('ticks')
    #sns.set_palette("bright")

    fig = plt.figure()
    fig.subplots_adjust(hspace=0.4, wspace=0.4)

    # PreHeat   + Diet I
    ax = fig.add_subplot(3, 3, 1)
    dfsub = df.query('Event == "PreHeat"  & Diet == "diet I" ')
    mypal = sns.color_palette("bright", 4, desat=1)
    sp = sns.lineplot(data=dfsub, x='Sample', y=traitnme, hue='ID', sharex=True,
                      alpha=0.925, palette=mypal, lw=2, marker="o")
    sp.set_ylim(df[traitnme].min(), df[traitnme].max())

    sp.grid(False)
    sp.get_legend().remove()



    # Heat   + Diet I
    ax = fig.add_subplot(3, 3, 2)
    dfsub = df.query('Event == "Heat"  & Diet == "diet I" ')
    mypal = sns.color_palette("bright", 4, desat=1)
    sp = sns.lineplot(data=dfsub, x='Sample', y=traitnme, hue='ID', sharex=True,
                      alpha=0.925, palette=mypal, lw=2, marker="o")
    sp.set_ylim(df[traitnme].min(), df[traitnme].max())

    sp.grid(False)
    sp.get_legend().remove()

    # Recovery   + Diet I
    ax = fig.add_subplot(3, 3, 3)
    print(df.Event.unique())

    dfsub = df.query('Event == "Recovery"  & Diet == "diet I" ')
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

