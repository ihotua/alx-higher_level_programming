#!/usr/bin/python3
def best_score(a_dictionary):
    best_key = None
    best_score = float('-inf')

    for k, v in a_dictionary.items():
        if v > best_score:
           best_score = v
           best_key = k

    return (best_key)
