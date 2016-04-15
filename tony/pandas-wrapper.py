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


def getValue(series, *labels):
    '''Retrieve label-n-value from n-level series.
    '''
    result = series
    i = 0
    try:
        for l in labels:
            indexLambda = getIndexLambda(thisSeries)
            result = indexLambda(l)
            i = i + 1
    except KeyError, e:
        if i < len(labels):
            return pd.DataFrame().sum()
        else:
            return 0

def getIndexLambda(series):
    return lambda i: series.ix[i]


def main():
    df = pd.DataFrame({ 'A' : 1.,
        'B' : pd.Timestamp('20130102'),
        'C' : pd.Series(1,index=list(range(4)),dtype='float32'),
        'D' : np.array([3] * 4,dtype='int32'),
        'E' : pd.Categorical(["test","train","test","train"]),
        'F' : 'foo' })


if __name__ == '__main__':
    main()
