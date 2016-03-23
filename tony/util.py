'''
    Util module of tony
'''

# Verify that an object is iterable if it implemented the iterator protocol
def isiterable(obj):
'''This function would return Truefor strings as well as most Python collection types'''
    try:
        iter(obj)
        return True
    except TypeError: # not iterable
        return False
        