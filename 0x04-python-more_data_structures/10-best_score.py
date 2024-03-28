#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    
    ihotu_key = next(iter(a_dictionary))
    alexa_value = a_dictionary[ihotu_key]

    for key, value in a_dictionary.items():
        if value > alexa_value:
            alexa_value = value
            ihotu_key = key

    return (ihotu_key)
