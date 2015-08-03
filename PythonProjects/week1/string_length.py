__author__ = 'Abdul'

"""
Define a function that computes the length of a given list or string
You can't use the builtin `len` function, you must use a for loop.
Example:
    length('hello')  # Should return 5
"""

def length(a_string):
    counter = 0
    for i in a_string:
        counter += 1
    return counter

