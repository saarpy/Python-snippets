'''
    util module of tony
'''

# Verify that an object is iterable if it implemented the iterator protocol
def isiterable(obj):
    '''This function would return Truefor strings as well as most Python collection types'''
    try:
        iter(obj)
        return True
    except TypeError: # not iterable
        return False

# make a list of the operations you want to apply to a particular set of strings:
def remove_punctuation(value):
    return re.sub('[!#?]', '', value)

clean_ops = [str.strip, remove_punctuation, str.title]

def clean_strings(strings, ops):
    result = []
    for value in strings:
        for function in ops:
            value = function(value)
        result.append(value)
    return result
