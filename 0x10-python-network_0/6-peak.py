#!/usr/bin/python3

def find_peak(list_of_integers):
    if not list_of_integers:
        return None

    mid = len(list_of_integers) // 2
    peak = list_of_integers[mid]

    if (mid == 0 or peak >= list_of_integers[mid - 1]) and (mid == len(list_of_integers) - 1 or peak >= list_of_integers[mid + 1]):
        return peak
    elif mid > 0 and peak < list_of_integers[mid - 1]:
        return find_peak(list_of_integers[:mid])
    else:
        return find_peak(list_of_integers[mid + 1:])
