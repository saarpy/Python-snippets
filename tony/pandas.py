'''
    Pandas module of tony
'''

import numpy as np
import pandas as pd

# TODO: only 2-level, too specific, need extension
def getVectorL2(series, label):
    '''Retrieve label-1-level vector from 2-level series.
    '''
    try:
        return series.ix[label]
    except KeyError, e:
        return pd.DataFrame().sum()

def getValueL2(series, label1, label2):
    '''Retrieve label-2-value from 2-level series.
    '''
    try:
        return series.ix[label1].ix[label2]
    except KeyError, e:
        return 0
