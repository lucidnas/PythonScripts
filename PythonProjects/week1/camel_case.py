__author__ = 'Abdul'


def camel_case(a_string):
    s = a_string.split()
    slist = [i.capitalize() for i in s]
    s = ' '.join(slist)
    return s

camel_case('hello world')


def divisible_numbers(a_list, a_list_of_terms):
    l = [[i for i in a_list_of_terms] for j in a_list if a_list[j] % a_list_of_terms[j] ==0]
    return l