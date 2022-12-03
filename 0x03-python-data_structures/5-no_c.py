#!/usr/bin/env python3
def no_c(my_string):
    # copy charcters from a string except c and C
    new = [x for x in my_string if not(x in 'cC')]

    return (''.join(str(e) for e in new))
