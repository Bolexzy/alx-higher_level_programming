#!/usr/bin/env python3
def no_c(my_string):
    ''' copy charcters from a string except c and C '''
    my_dict = {ord(i): None for i in 'cC'}
    new_string = my_string.translate(my_dict)

    return new_string
