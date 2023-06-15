#!/usr/bin/python3
def best_score(a_dictionary):
    if not isinstance(a_dictionary, dict) or len(a_dictionary) == 0:
        return None

    re = list(a_dictionary.keys())[0]
    bi = a_dictionary[re]
    for i, j in a_dictionary.items():
        if j > bi:
            bi = j
            re = i
    return (re)
