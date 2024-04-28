import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import collections
import random
import numpy as np


class myResearch:
    def __init__(self,file):
        # get pandas dataframe data set
        self.df = pd.read_csv(file, sep=';')
        self.lW, self.uW = self.calcIQR()

    def generateMissingVal(self, ml):
        '''Generate missing values in dataset
        Args:
            ml (float): missing values level - range: 0-1
        '''
        df = self.df
        replaced = collections.defaultdict(set)
        ix = [(row, col) for row in range(df.shape[0]) for col in range(df.shape[1])]
        random.shuffle(ix)
        to_replace = int(round(ml * len(ix)))

        for row, col in ix:
            if len(replaced[row]) < df.shape[1] - 1:
                df.iloc[row, col] = np.nan
                to_replace -= 1
                replaced[row].add(col)
                if to_replace == 0:
                    break

    def calcIQR(self):
        '''Define the range of Interquartile Ranges (IQRs) and apply them to the dataset to identify the outliers.
        Args:

        Returns:
            lw (pandas.core.series.Series): lower 1.5*IQR whisker
            uW (pandas.core.series.Series): upper 1.5*IQR whisker
        '''
        df = self.df
        num = df._get_numeric_data()
        Q1 = num.quantile(0.25)
        Q3 = num.quantile(0.75)
        IQR = Q3 - Q1
        lW = Q1 - 1.5 * IQR
        uW = Q3 + 1.5 * IQR
        return lW, uW

    def showOutliers(self,col,kind):

        df=self.df
        lW=self.lW
        uW=self.uW

        if (kind == 'upper'):
            return df[(df[col] > uW[col])]
        if (kind == 'lower'):
            return df[(df[col] < lW[col])]
        if (kind == 'both'):
            return df[(df[col] > uW[col]) | (df[col] < lW[col])]

    def plotOutliers(self,col):

        df = self.df
        sns.boxplot(data=df, y=col)

