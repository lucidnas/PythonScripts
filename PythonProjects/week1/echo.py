__author__ = 'Abdul'

def echo():
    s = input('Insert a string: ')
    if s != 'quit':
        print(s)
        echo()
    else:
        return 'bye'


echo()
