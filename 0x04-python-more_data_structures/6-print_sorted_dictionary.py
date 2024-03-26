#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    ihotu = sorted(a_dictionary.k())

    for k in ihotu:
        print("{}: {}".format(k, a_dictionary[k]))
