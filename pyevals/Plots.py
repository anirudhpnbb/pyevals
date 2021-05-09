import seaborn as sns
from matplotlib import pyplot as plt
from PyPDF2 import PdfFileMerger, PdfFileReader
import os
import shutil
from utils import *
import warnings

warnings.filterwarnings('ignore')


def MakePlots(df, cat_features, con_features, filename="Plots"):
    mergedObject = PdfFileMerger()

    if os.path.exists(filename):
        shutil.rmtree(filename)

    os.mkdir(filename)
    os.chdir(filename)
    os.chmod(filename, 777)

    # Heat Map
    h, axs = plt.subplots()
    sns.heatmap(df.corr())
    axs.set_title('HeatMap :- ')
    plt.savefig("HeatMap.pdf")

    # DistPlot
    TotalDistPlots = len(con_features)
    f, axes = plt.subplots(CalcuateRows(TotalDistPlots), 3, figsize=(10, 10))

    column = 0
    row = 0
    while row < TotalDistPlots:
        for i in con_features:
            if column < 3:
                try:
                    axes[row, column].set_title('DistPlot :- ' + i)
                    sns.distplot(df[i], ax=axes[row, column])
                    column += 1
                    if column == 3:
                        row += 1
                        column = 0
                except:
                    print("", end="")
        row += 1
    plt.savefig("DistPlots.pdf")
    plt.tight_layout()

    # CountPlot
    TotalCountPlots = len(cat_features)
    f, axes = plt.subplots(CalcuateRows(TotalCountPlots), 3, figsize=(10, 10))

    column = 0
    row = 0

    while row < TotalCountPlots:
        for i in cat_features:
            if column < 3:
                try:
                    axes[row, column].set_title('CountPlot :- ' + i)
                    sns.countplot(df[i], ax=axes[row, column])
                    column += 1
                    if column == 3:
                        row += 1
                        column = 0
                except:
                    print("", end="")
        row += 1
    plt.savefig("CountPlots.pdf")
    plt.tight_layout()

    # Bar Plot
    TotalBarPlots = len(cat_features)
    f, axes = plt.subplots(CalcuateRows(TotalBarPlots), 3, figsize=(10, 10))

    column = 0
    row = 0

    while row < TotalBarPlots:
        for i in con_features:
            for j in cat_features:
                if column < 3:
                    try:
                        axes[row, column].set_title('BarPlot :- ' + i + ' Vs ' + j)
                        sns.barplot(x=i, y=j, data=df, ax=axes[row, column])
                        column += 1
                        if column == 3:
                            row += 1
                            column = 0
                    except:
                        print("", end="")
        row += 1
    plt.savefig("BarPlots.pdf")
    plt.tight_layout()

    # Box Plot
    TotalBoxPlots = len(cat_features)
    f, axes = plt.subplots(CalcuateRows(TotalBoxPlots), 3, figsize=(10, 10))

    column = 0
    row = 0

    while row < TotalBoxPlots:
        for i in con_features:
            for j in cat_features:
                if column < 3:
                    try:
                        axes[row, column].set_title('BoxPlot :- ' + j + ' Vs ' + i)
                        sns.boxplot(x=j, y=i, data=df, ax=axes[row, column])
                        column += 1
                        if column == 3:
                            row += 1
                            column = 0
                    except:
                        print("", end="")
        row += 1
    plt.savefig("BoxPlots.pdf")
    plt.tight_layout()

    # Violin Plot
    TotalViolinPlots = len(cat_features)
    f, axes = plt.subplots(CalcuateRows(TotalViolinPlots), 3, figsize=(10, 10))

    column = 0
    row = 0

    while row < TotalViolinPlots:
        for i in con_features:
            for j in cat_features:
                if column < 3:
                    try:
                        axes[row, column].set_title('ViolinPlot :- ' + i + ' Vs ' + j)
                        sns.violinplot(x=i, y=j, data=df, ax=axes[row, column])
                        column += 1
                        if column == 3:
                            row += 1
                            column = 0
                    except:
                        print("", end="")
        row += 1
    plt.savefig("ViolinPlots.pdf")
    plt.tight_layout()

    # Pair Plot
    a = sns.pairplot(df)
    a.fig.suptitle('PairPlot :- ')
    plt.savefig("PairPlot.pdf")

    for i in cat_features:
        a = sns.pairplot(df, hue=i)
        a.fig.suptitle("PairPlot :- " + i)
        plt.savefig("PairPlot%s.pdf" % i)

    CurrentDirectory = os.getcwd()
    AllFiles = os.listdir(CurrentDirectory)

    for file in AllFiles:
        if file.endswith('.pdf'):
            mergedObject.append(PdfFileReader(file, 'rb'))

    mergedObject.write("FinalPlots.pdf")
    os.chdir('../')
