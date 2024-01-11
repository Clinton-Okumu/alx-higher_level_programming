#!/usr/bin/python3
def copy_list(lst):
    return lst.copy() if isinstance(lst, list) else lst
