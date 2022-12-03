#!/usr/bin/env python3
def no_c(my_string):
    ''' copy charcters from a string except c and C '''
    new = [x for x in my_string if x != 'c' and x != 'C']

    return (''.join(str(e) for e in new))
