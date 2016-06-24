'''
    myio.py
    SNLP.UdS.SS16
    @author: Tony Hong
'''

import os


def read_file(path):
    '''
    read raw text from file
    '''
    raw_text = open(path, 'r').read().decode('utf-8')
    return raw_text


def get_file_dict(container, file_dir, sp_filetype=''):
    result = dict()
    if type(container) == type({}):
        filenames = container.itervalues()
    elif type(container) == type([]):
        filenames = container
    else:
        return result

    if sp_filetype:
        suffix = '.' + sp_filetype
    else:
        suffix = ''

    for k in filenames:
        names = k.split('.')
        name = names[0]
        if suffix:
            result[name] = os.path.join(file_dir, name + suffix)
        else:
            result[name] = os.path.join(file_dir, k)

    return result

def get_text_dict(file_dict):
    '''
    set up text dict from file dict
    '''
    result = dict()
    for k, v in file_dict.iteritems():
        result[k] = read_file(v)
    return result
