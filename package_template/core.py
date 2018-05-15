import numpy as np
import pandas as pd
from scipy.stats import gaussian_kde


def mymodel(x, kind='kde', bins=15):
    """Example function

    This example function will take an input numpy array or pandas.Series and
    either output a histogram or kernel density estimate. This should just
    illustrate how you can implement your own code.

    Parameters
    ----------
    x : numpy.ndarray, pandas.Series
        Either a Series or an array that will be used to plot the distribution.
    kind : string
        Specify the kind of plot. Can either be 'kde' for a kernel density
        estimate, or 'hist' for a histogram
    bins : 15
        Specify the number of bins to be aranged between the minimum and
        maximum observation.

    Returns
    -------
    matplotlib.Axes

    """
    # check the input dtype
    if not isinstance(x, (np.ndarray, pd.Series)):
        raise ValueError('Please use a numpy array or pandas Series as input')

    if not (isinstance(kind, str) and kind in ('kde', 'hist')):
        raise ValueError("kind has to be one of 'kde', 'hist'")

    if not (isinstance(bins, int) and bins > 0):
        raise ValueError('bins has to be a positive integer')

    # make the array a Series
    if isinstance(x, pd.Series):
        array = x.values
    else:
        array = x

    # claculate a gaussian kernel density estimate
    if kind == 'kde':
        kde = gaussian_kde(array)
        counts = kde.evaluate(np.linspace(np.min(array), np.max(array), 15))

    # otherwise 'hist' was passed
    else:
        counts = np.histogram(array, bins=bins)[0]

    # calculate and return the density
    return counts / np.sum(counts)


