#!/usr/bin/env python3
def no_c(my_string):
    while 'c' in my_string or 'C' in my_string:
        my_string = my_string.replace('c', '').replace('C', '')

    return my_string
