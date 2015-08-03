from __future__ import division

__author__ = 'Abdul'

"""
Write a function that receives 2 numbers and performs simple calculations
(additions, subtractions, multiplications and divisions)
based on a string parameter.
Example:
    calculator(2, 3, 'add')       # Should return 5
    calculator(7, 3, 'subtract')  # Should return 4
    calculator(2, 7, 'multiply')  # Should return 14
    calculator(8, 4, 'divide')    # Should return 2
    calculator(5, 2, 'divide')    # Should return 2.5 ATTENTION!
"""

def calculator(param1, param2, operation):
    if operation == 'add':
        return param1 + param2
    elif operation == 'subtract':
        return param1 - param2
    elif operation == 'multiply':
        return param1 * param2
    elif operation == 'divide':
            print param1 / param2
            return param1 / param2


calculator(8,2,'divide')


'''if operation == 'divide' and param1 % param2 == 0 and param1 >= param2:
            print param1 / (float)param2
            return param1 / param2
        else:
            print(float(param1) / param2)
            return float(param1) / param2
        '''