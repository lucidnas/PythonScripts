__author__ = 'Abdul'

"""
Write a function that receives a list and returns the larger number in the list.
Example:
    max_in_list([7, 1, 5, 8, 0, 7, 9, 1, 7])
    > 9

Extras:
* Try with a for loop
* Try with a while loop
* Investigate special list methods or python libraries.
"""

def max_in_list(a_list):
    j = 0
    for i in a_list:
        if i > j:
            j = i
    return j