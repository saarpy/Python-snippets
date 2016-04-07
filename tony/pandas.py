'''
    pandas module of tony
'''

import numpy as np
import pandas as pd

'''
    Retrieve label1-level vector from 2-level series
'''
def getVector(series, label):
    try:
        return series.ix[label]
    except KeyError, e:
        return pd.DataFrame().sum()

def getValue(series, label1, label2):
    try:
        return series.ix[label].ix[labe2]
    except KeyError, e:
        return 0