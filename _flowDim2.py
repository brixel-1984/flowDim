# Script to compute the time evolution of flow dimensions for subradial flows

import numpy as np
import pandas as pd

def indices(a, func):
    """
    return index
    """

    return [i for (i,val) in enumerate(a) if func(val)]


def hyclean(self, df=None):
    """
    hyclean: Take only the values that are not nan, finite and strictly positive time.
    :param df:  pandas DF expects at least two traces in the dataframe.
    The first column needs to be the time and the second the data trace.
    :return df: pandas series gives back the cleaned dataset
    """

    if df is not None:
        self.df = df

    self.header()
    df = self.df.replace([np.inf, -np.inf], np.nan)
    for i in range(1, len(self.hd)):
        self.df = df[df[self.hd[i]] >= 0]

    return self.df


def flowDim2(self, df=None):
    """
    computes the time evolution of flow dimensions

    Syntax:
        x_dim, y_dim = flowDim(t,s)
        t = elapsed time
        s = drawdown or pressure buildup
    """

    if df is not None:
        self.df = df

    self.header()

    # remove all NaN. Keep finite, strictle positive 
    self.hyclean()

    x = self.df[self.hd[0]][1:]

    # compute flow dimension
    y = np.multiply(3, (1 - np.divide(([np.log10(x) - np.log10(self.df[self.hd[1]][i - 1]) for i, x in enumerate(self.df[self.hd[1]]) if i > 0]), [
        np.log10(x) - np.log10(self.df[self.hd[0]][i - 1]) for i, x in enumerate(self.df[self.hd[0]]) if i > 0])))
    dummy = np.array(np.transpose([x, y]))
    self.dim = pd.DataFrame(dummy, columns=self.hd)
    return self.dim    