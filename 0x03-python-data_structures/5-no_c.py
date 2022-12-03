#!/usr/bin/env python3
def no_c(my_string):
    # copy charcters from a string except c and C
    new_string = [x for x in my_string if not(x in 'cC')]
    return ("".join(new_string))
