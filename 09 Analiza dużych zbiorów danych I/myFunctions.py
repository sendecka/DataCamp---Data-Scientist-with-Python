import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import collections
import random
import numpy as np


def generateMissingVal(df, ml):
    ''' Generate missing values in dataset
    Args:
        df (pandas.core.frame.DataFrame): pandas dataframe data set
        ml (float): missing values level - range: 0-1
    '''
    import random
    # collect the indexes (row, col) from dataframe
    replaced = collections.defaultdict(set)
    ix = [(row, col) for row in range(df.shape[0]) for col in range(df.shape[1])]
    # randomly shuffle the collection of indexes
    random.shuffle(ix)
    # set the ammount of replaced values at level of 10%
    to_replace = int(round(ml * len(ix)))
    # perform replacing of existing values with missing values
    for row, col in ix:
        if len(replaced[row]) < df.shape[1] - 1:
            df.iloc[row, col] = np.nan
            to_replace -= 1
            replaced[row].add(col)
            if to_replace == 0:
                break


def calcIQR(df):
    '''Define the range of Interquartile Ranges (IQRs) and apply them to the dataset to identify the outliers.
    Args:
        df (pandas.core.frame.DataFrame): pandas dataframe data set
    Returns:
        lw (pandas.core.series.Series): lower 1.5*IQR whisker
        uW (pandas.core.series.Series): upper 1.5*IQR whisker
        '''
    # get only numeric data frame from dataframe
    num = df._get_numeric_data()
    # calc first quartile Q1
    Q1 = num.quantile(0.25)
    # calc third quartile Q3
    Q3 = num.quantile(0.75)
    # calc interquatile range IRQ
    IQR = Q3 - Q1
    # calc lower 1.5*IQR whisker
    lW = Q1 - 1.5 * IQR
    # calc upper 1.5*IQR whisker
    uW = Q3 + 1.5 * IQR
    return lW, uW


def showOutliers(col, df, uW, lW, kind):
    '''Show chosen outliers records from dataframe.
    Args:
        col(string): datafrme column name
        df (pandas.core.frame.DataFrame): pandas dataframe data set
        uW (pandas.core.series.Series): upper 1.5*IQR whisker
        lW (pandas.core.series.Series): lower 1.5*IQR whisker
        kind (string): kind of outlier, acceptable values are: 'upper', 'lower', 'both'
    Returns:
        (pandas.core.frame.DataFrame): pandas dataframe data set with outliers records'''

    # show upper outliers for age
    if kind == 'upper':
        df[(df[col] > uW[col])]
    elif kind == 'lower':
        df[(df[col] < lW[col])]
    elif kind == 'both':
        return df[(df[col] > uW[col]) | (df[col] < lW[col])]


def plotOutliers(col, df):
    '''Plot boxplot for chosen column from dataframe
    Args:
        col(string): dataframe column name
        df(pandas.core.frame.DataFrame): pandas dataframe data set
    '''

    import seaborn as sns
    import matplotlib.pyplot as plt
    sns.boxplot(data=df, y=col)

