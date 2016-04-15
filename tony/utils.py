'''
    Utilities module of Tony
'''

def isiterable(obj):
    '''Verify that an object is iterable if it implemented the iterator protocol.

    This function would return True for strings as well as most Python collection types.
    '''
    try:
        iter(obj)
        return True
    except TypeError: # not iterable
        return False


def remove_punctuation(value):
    '''make a list of the operations you want to apply to a particular set of strings.
    '''
    return re.sub('[!#?]', '', value)

clean_ops = [str.strip, remove_punctuation, str.title]

def clean_strings(strings, ops):
    result = []
    for value in strings:
        for function in ops:
            value = function(value)
        result.append(value)
    return result
