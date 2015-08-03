__author__ = 'Abdul'

"""
Write a function that receives a list and an element and returns how many occurrences
of that particular element are in the list.
Example:
    occurrences([7, 1, 5, 8, 0, 7, 9, 1, 7], 7)  # The number 7 is repeated 3 times.
    > 3
Extras:
* Try with a for loop
* Try with a while loop
* Investigate special list methods or python libraries.
"""

def occurrences(a_list, an_element):
    counter = 0
    for i in a_list:
        if an_element == i:
            print i
            counter += 1
    return counter

occurrences([2,3,4,4,4,5], 4)