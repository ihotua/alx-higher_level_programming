#!/usr/bin/python3
def best_score(a_dictionary):
    ihotu_key = None
    alexa_value = float('-inf')

    for key, value in a_dictionary.items():
        if value > alexa_value:
            alexa_value = value
            ihotu_key = key

    return (ihotu_key)
