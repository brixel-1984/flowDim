# Script to compute the time evolution of flow dimensions for subradial flows

import numpy as np
import pandas as pd

def indices(a, func):
    """
    return index
    """

    return [i for (i,val) in enumerate(a) if func(val)]

def flowDim(t, s):
    """
    computes the time evolution of flow dimensions

    Syntax:
        x_dim, y_dim = flowDim(t,s)
        t = elapsed time
        s = drawdown or pressure buildup
    """

    t = np.asarray(t, dtype='float')
    s = np.asarray(s, dtype='float')

    # remove NaNs
    index_s = indices(s, lambda s: np.isfinite(s))
    xi = t[index_s]
    yi = s[index_s]

    # keep times>0 and corresponding observations
    xii = xi[np.argwhere((xi >= 0) & (yi >= 0)).flatten()]
    yii = yi[np.argwhere((yi >= 0) & (xi >= 0)).flatten()]

    x_dim = xii[1:]
    # compute flow dimension
    y_dim = np.multiply(2,(1 - np.divide(([np.log10(x) - np.log10(yii[i - 1]) for i, x in enumerate(yii) if i > 0]),[
        np.log10(x) - np.log10(xii[i - 1]) for i, x in enumerate(xii) if i > 0])))

    return x_dim, y_dim