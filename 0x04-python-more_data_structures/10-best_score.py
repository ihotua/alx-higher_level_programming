#!/usr/bin/python3
def best_score(a_dictionary):
    ihotu = None
    alexa = float('-inf')

    for key, value in a_dictionary.items():
        if value > alexa:
            alexa = value
            ihotu = key

    return (ihotu)
