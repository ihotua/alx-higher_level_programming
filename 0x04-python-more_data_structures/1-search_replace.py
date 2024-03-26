#!/usr/bin/python3
def search_replace(my_list, search, replace):
    sweet_list = []

    for element in my_list:
        if element == search:
            sweet_list.append(replace)
        else:
            sweet_list.append(element)

    return (sweet_list)
