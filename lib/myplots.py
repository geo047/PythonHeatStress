# Plotting functions
import pandas as pd
import seaborn as sns
import numpy as np
from matplotlib import pyplot as plt, patches
import matplotlib


def my_plot(df, traitnme:str, plottype:str):
    # sns.set_style("white", {'grid.color': "0.2", "grid.linestyle": "--"})
    # sns.set_context("notebook", rc={"grid.linewidth": 5})
    sns.set_style('ticks')
    # sns.set_context("notebook", rc={"grid.linewidth": 5})

    #sns.set_palette("bright")

    mypal = sns.color_palette("bright", 3, desat=1)


    # Use palplot and pass in the variable:


    sp = sns.lineplot(data=df, x='DayNumber', y=traitnme, hue='Diet', errorbar=('se', 1.96 ),
                      hue_order=['Diet I', 'Diet II', 'Diet III'], alpha=1, palette=mypal, lw=3,
                      legend = True)
    sp.set(xlabel="Day Number", ylabel= ('Mean within Diet')   , title= traitnme )
    #####!!!!!sp.grid(False)

    handles, labels = sp.get_legend_handles_labels()
    sp.legend(handles=handles[0:], labels=labels[0:])
    plt.legend(loc='upper right')
    plt.legend(fancybox=True, framealpha=0.1, loc='upper right')
 #   plt.setp(sp.get_legend().get_texts(), fontsize='14')
    plt.axvline(x=4.5, linestyle='dashed')
    plt.axvline(x=11.5, linestyle='dashed')
    if plottype == "y":
        sp.set(xlabel=None)
    if plottype == "x":
        sp.set(ylabel=None)
    if plottype == "none":
        sp.set(xlabel=None)
        sp.set(ylabel=None)
    #plt.show()

    sp.set_yticklabels(sp.get_yticks().round(3), size=13)
    sp.set_xticklabels(sp.get_xticks().round(3), size=13)
    return sp


def my_individual_plot(df, traitnme:str):

    sns.set_theme(style="ticks")

    palette = sns.color_palette("rocket_r")
    myid = df['ID'].unique()
    #myid.sort()  # sorts inplace
    myid = ['3795', '3793', '3796',
            '3799', '3794', '3798',
            '3801', '3797', '3803',
            '3802', '3805', '3804'
            ]

    g = sns.relplot(data=df, x="Sample", y=traitnme, hue="ID",
                    row="Diet", height = 5, aspect=0.75, style="ID", kind="line",
                    row_order=['Diet I', 'Diet II', 'Diet III'], markers="o",
                    linewidth=3,
                    hue_order=myid, palette=sns.color_palette("tab10", 3),
                    facet_kws={"margin_titles": True},
                    dashes = [(1,1),(2,1),(1,1),(1,1),(3,1),(2,1),(2,1),(3,1),(4,1),(3,1),(4,1),(4,1) ]
                    )


    lenofarray = len(df['Sample'].unique())
    lenofarray += 1
    g.set(xticks=np.arange(1, lenofarray, 1))
    g.set_xticklabels(np.arange(1, lenofarray, 1) )


    g.set_titles(col_template="{col_name}", row_template="{row_name}")

    g.set_ylabels(traitnme, clear_inner=False)
    g.set_xlabels("Day Number",  clear_inner=False)
    g.fig.suptitle(traitnme, fontsize=16)
    g.fig.subplots_adjust(top=0.9, bottom=0.1)
    g.legend.remove()
    #plt.show()



    sns.set(font_scale=0.5)
    sns.set_style('ticks')

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
    #print(df.Event.unique())

    dfsub = df.query('Event == "Recovery"  & Diet == "diet I" ')
    mypal = sns.color_palette("bright", 4, desat=1)
    sp = sns.lineplot(data=dfsub, x='Sample', y=traitnme, hue='ID', sharex=True,
                      alpha=0.925, palette=mypal, lw=2, marker="o")
    sp.set_ylim(df[traitnme].min(), df[traitnme].max())

    sp.grid(False)
    sp.get_legend().remove()

    #plt.show()



#
# def rect_plot(df, min_neg, max_pos):
#     plt.rcParams["figure.figsize"] = [7.00, 7.00]
#     plt.rcParams["figure.autolayout"] = True
#
#     fig = plt.figure()
#     ax = fig.add_subplot(111)
#
#     #          Heat      Recovery
#     #        +---------------------+
#     #   D1   | D1-D3   |  D1-D3    |
#     #        |-------  + ----------|
#     #   D2   | D2-D3   |  D2-D3    |
#     #        +---------------------+
#     #  Upper Left
#     val = df.iat[1, 1]
#     if val < 0:
#         cmap = matplotlib.pyplot.get_cmap('Greys')
#         rgba = cmap(val/min_neg)
#         matplotlib.pyplot.text(x=-4, y=2, s="Heat: D1 - D3", fontsize=18, color="blue")
#     else:
#         cmap = matplotlib.pyplot.get_cmap('Reds')
#         rgba = cmap(val/max_pos)
#         ax = matplotlib.pyplot.text(x=-4, y=2, s="Heat: D1 - D3", fontsize=18, color="blue")
#     rectD1H = patches.Rectangle((-5, 0), 5, 5, facecolor= rgba , linewidth=1)
#
#
#     val = df.iat[3, 1]
#     if val < 0:
#         cmap = matplotlib.pyplot.get_cmap('Greys')
#         rgba = cmap(val/min_neg)
#         matplotlib.pyplot.text(x=1, y=2, s="Rec: D1 - D3", fontsize=18, color="blue")
#     else:
#         cmap = matplotlib.pyplot.get_cmap('Reds')
#         rgba = cmap(val/max_pos)
#         matplotlib.pyplot.text(x=1, y=2, s="Rec: D1 - D3", fontsize=18, color="blue")
#     rectD1R = patches.Rectangle((0, 0), 5, 5, facecolor=rgba, linewidth=1)
#
#     val = df.iat[2, 1]
#     if val < 0:
#         cmap = matplotlib.pyplot.get_cmap('Greys')
#         rgba = cmap(val/min_neg)
#         matplotlib.pyplot.text(x=-4, y=-2, s="Heat: D2 - D3", fontsize=18, color="blue")
#     else:
#         cmap = matplotlib.pyplot.get_cmap('Reds')
#         rgba = cmap(val/max_pos)
#         matplotlib.pyplot.text(x=-4, y=-2, s="Heat: D2 - D3", fontsize=18, color="blue" )
#     rectD2H = patches.Rectangle((-5, -5), 5, 5, facecolor=rgba, linewidth=1)
#
#
#
#     val = df.iat[4, 1]
#     if val < 0:
#         cmap = matplotlib.pyplot.get_cmap('Greys')
#         rgba = cmap(val/min_neg)
#         matplotlib.pyplot.text(x=1, y=-2, s="Rec: D2 - D3", fontsize=18, color= "blue")
#     else:
#         cmap = matplotlib.pyplot.get_cmap('Reds')
#         rgba = cmap(val/max_pos)
#         matplotlib.pyplot.text(x=1, y=-2, s="Rec: D2 - D3", fontsize=18, color= "blue")
#     rectD2R = patches.Rectangle((0, -5), 5, 5, facecolor=rgba, linewidth=1)
#
#     ax.add_patch(rectD1H)
#     ax.add_patch(rectD1R)
#     ax.add_patch(rectD2H)
#     ax.add_patch(rectD2R)
#
#     plt.xlim([-5, 5])
#     plt.ylim([-5, 5])
#     plt.title(df.trait[0])
#     plt.axis("off")
#     return ax

def rect_plot(fig, ax, df, min_neg, max_pos):
    # Plot superceded. Too difficult to interpret differences. Contrast
    # diff could be due to aa number of different situations in the estimates.
    # Going for bar plots of straight Diet level estimates instead. See below

    plt.rcParams["figure.figsize"] = [7.00, 7.00]
    plt.rcParams["figure.autolayout"] = True

    #          Heat      Recovery
    #        +---------------------+
    #   D1   | D1-D3   |  D1-D3    |
    #        |-------  + ----------|
    #   D2   | D2-D3   |  D2-D3    |
    #        +---------------------+
    #  Upper Left
    val = df.iat[1, 1]
    if val < 0:
        cmap = matplotlib.pyplot.get_cmap('Greys')
        rgba = cmap(val/min_neg)
        matplotlib.pyplot.text(x=-4, y=2, s="Heat: D1 - D3", fontsize=4, color="blue")
    else:
        cmap = matplotlib.pyplot.get_cmap('Reds')
        rgba = cmap(val/max_pos)
        matplotlib.pyplot.text(x=-4, y=2, s="Heat: D1 - D3", fontsize=4, color="blue")
    rectD1H = patches.Rectangle((-5, 0), 5, 5, facecolor= rgba , linewidth=1)


    val = df.iat[3, 1]
    if val < 0:
        cmap = matplotlib.pyplot.get_cmap('Greys')
        rgba = cmap(val/min_neg)
        matplotlib.pyplot.text(x=1, y=2, s="Rec: D1 - D3", fontsize=4, color="blue")
    else:
        cmap = matplotlib.pyplot.get_cmap('Reds')
        rgba = cmap(val/max_pos)
        matplotlib.pyplot.text(x=1, y=2, s="Rec: D1 - D3", fontsize=4, color="blue")
    rectD1R = patches.Rectangle((0, 0), 5, 5, facecolor=rgba, linewidth=1)

    val = df.iat[2, 1]
    if val < 0:
        cmap = matplotlib.pyplot.get_cmap('Greys')
        rgba = cmap(val/min_neg)
        matplotlib.pyplot.text(x=-4, y=-2, s="Heat: D2 - D3", fontsize=4, color="blue")
    else:
        cmap = matplotlib.pyplot.get_cmap('Reds')
        rgba = cmap(val/max_pos)
        matplotlib.pyplot.text(x=-4, y=-2, s="Heat: D2 - D3", fontsize=4, color="blue" )
    rectD2H = patches.Rectangle((-5, -5), 5, 5, facecolor=rgba, linewidth=1)



    val = df.iat[4, 1]
    if val < 0:
        cmap = matplotlib.pyplot.get_cmap('Greys')
        rgba = cmap(val/min_neg)
        matplotlib.pyplot.text(x=1, y=-2, s="Rec: D2 - D3", fontsize=4, color= "blue")
    else:
        cmap = matplotlib.pyplot.get_cmap('Reds')
        rgba = cmap(val/max_pos)
        matplotlib.pyplot.text(x=1, y=-2, s="Rec: D2 - D3", fontsize=4, color= "blue")
    rectD2R = patches.Rectangle((0, -5), 5, 5, facecolor=rgba, linewidth=1)

    ax.add_patch(rectD1H)
    ax.add_patch(rectD1R)
    ax.add_patch(rectD2H)
    ax.add_patch(rectD2R)

    plt.xlim([-5, 5])
    plt.ylim([-5, 5])
    plt.title(df.trait[0], fontdict={'fontsize': 6})
    plt.axis("off")

    return fig


def my_bar_plot(df, eventType):
    # bar plot of standardized estimates of Diet 1, II, and III for Event type
    X = df.trait.unique()
    D1 = df['emmean'][(df.Diet == "Diet I") & (df.Event == eventType)]
    D2 = df['emmean'][(df.Diet == "Diet II") & (df.Event == eventType)]
    D3 = df['emmean'][(df.Diet == "Diet III") & (df.Event == eventType)]



    # Ygirls = [10, 20, 20, 40]
    # Zboys = [20, 30, 25, 30]

    X_axis = np.arange(len(X))

    # Set position of bar on X axis
    barWidth = 0.25
    br1 = np.arange(len(X))
    br2 = [x + barWidth for x in br1]
    br3 = [x + barWidth for x in br2]


    plt.bar(br1, D1, width=barWidth, label='Diet I')
    plt.bar(br2, D2, width=barWidth, label='Diet II')
    plt.bar(br3, D3, width=barWidth, label='Diet II')

    plt.xticks(X_axis, X)
    plt.xlabel("Responses")
    plt.ylabel("Standardized Effect Size")
    plt.title( eventType + ' Event', fontsize = 16)
    plt.legend()
    plt.xticks(rotation=90)  # Rotates X-Axis Ticks by 45-degrees

    filenm = "/home/g/PyCharm/PythonHeatStress/fig" + eventType + ".pdf"
    plt.savefig(filenm)


    #plt.show()